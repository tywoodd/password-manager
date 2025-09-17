from dataclasses import dataclass, field
from datetime import datetime
import json
import os, base64
from typing import NamedTuple
from db import init_db, SessionLocal
from models import KDFPolicy, VaultData, VaultKey
from argon2.low_level import hash_secret_raw, Type
from getpass import getpass
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag


_AAD_WRAP = b"wrap:v1"
_AAD_DATA = b"data:v1"


class KeyRef(NamedTuple):
    key_id: int
    policy_id: int


@dataclass(slots=True)
class UnlockedVault:
    key_id: int
    policy_id: int
    dek: bytearray = field(repr=False, compare=False, hash=False)


def aad_for_wrap(policy_id: int, kdfv: int) -> bytes:
    return b";".join([_AAD_WRAP,
                      f"policy_id={policy_id}".encode(),
                      f"kdfv={kdfv}".encode()])


# Get the KDF Policy data, creates new row if non-existant. This is used when deriving the KEK (Key Encryption Key).
def get_or_create_policy(session):
    existing = session.query(KDFPolicy).order_by(KDFPolicy.id.asc()).first()
    if existing:
        return existing

    salt = os.urandom(16)
    salt_b64 = base64.b64encode(salt).decode("utf-8")

    policy = KDFPolicy(salt_b64=salt_b64)

    session.add(policy)
    session.commit()
    session.refresh(policy)

    return policy



# Derives KEK (Key Encryption Key). This is used to wrap and unwrap the DEK (Data Encryption Key), which will encrypt and decrypt the password vault. Uses KDF Policy for parameters.
def derive_kek(master_password: str, policy) -> bytes:

    # Decode and validate salt
    try:
        salt = base64.b64decode(policy.salt_b64, validate=True)
    except Exception as e:
        raise ValueError("Invalid Base64 in policy.salt_b64") from e
    
    if len(salt) < 16:
        raise ValueError("Salt must be at least 16 bytes")


    kek = hash_secret_raw(
        secret=master_password.encode("utf-8"),
        salt=salt,
        time_cost=policy.time_cost,
        memory_cost=policy.memory_cost,
        parallelism=policy.parallelism,
        hash_len=policy.hash_len,
        type=Type.ID
    )
    return kek


# Generate new DEK wrapped and stored in vault_keys table.
def generate_new_dek(session, kek: bytes, policy: "KDFPolicy") -> KeyRef:
    dek = os.urandom(32)
    nonce = os.urandom(12)

    aesgcm = AESGCM(kek)
    aad = aad_for_wrap(policy_id=policy.id, kdfv=policy.kdf_version)

    ciphertext = aesgcm.encrypt(nonce=nonce, data=dek, associated_data=aad)

    vault_key = VaultKey(
        ciphertext=ciphertext,
        nonce=nonce,
        policy_id=policy.id,
        active=True
    )

    session.add(vault_key)
    session.commit()
    

    return KeyRef(
        key_id=vault_key.id, 
        policy_id=vault_key.policy_id
    )


def get_or_create_active_key_ref(session, kek, policy) -> KeyRef:
    row = (session.query(VaultKey.id, VaultKey.policy_id)
                  .filter_by(active=True)
                  .one_or_none())
    if row is None:
        # Creates, wraps, persists; returns KeyRef (ids only)
        return generate_new_dek(session=session, kek=kek, policy=policy)
    return KeyRef(key_id=row.id, policy_id=row.policy_id)


# Unwrap DEK. Returns the created DEK to encrypt new entries and decrypt existing entries in the vault_data table.
def unwrap_dek(session, kek: bytes, key_ref: KeyRef, policy: "KDFPolicy") -> UnlockedVault:
    row = (session.query(
                VaultKey.id,
                VaultKey.ciphertext,
                VaultKey.nonce, 
                VaultKey.policy_id,
                VaultKey.active
           )
           .filter(VaultKey.id == key_ref.key_id)
           .one_or_none())

    aad = aad_for_wrap(policy_id=policy.id, kdfv=policy.kdf_version)

    try:
        dek_bytes = AESGCM(kek).decrypt(
            nonce=row.nonce,
            data=row.ciphertext,
            associated_data=aad
        )
    except InvalidTag as e:
        # Wrong KEK or tampered blob
        raise "unable to unwrap DEK" from e
    
    vault = UnlockedVault(
        key_id=row.id,
        policy_id=row.policy_id,
        dek=bytearray(dek_bytes)
    )

    del dek_bytes
    return vault


def main():
    # Create vault.db
    init_db()
    session = SessionLocal()

    # Get or create kdf_policies table with policy row
    policy = get_or_create_policy(session)

    # Derive KEK using master_password and kdf_policies
    master_password = getpass("Enter master password: ")
    kek = derive_kek(master_password=master_password, policy=policy)
    del master_password

    # Obtain unwrapped DEK to write and read vault_data 
    key_ref = get_or_create_active_key_ref(session=session, kek=kek, policy=policy)    
    vault = unwrap_dek(session=session, key_ref=key_ref, kek=kek, policy=policy)   

    print(vault)


if __name__ == "__main__":
    main()


