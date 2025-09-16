from datetime import datetime
import json
import os, base64
from typing import TypedDict
from db import init_db, SessionLocal
from models import KDFPolicy, VaultData, VaultKey
from argon2.low_level import hash_secret_raw, Type
from getpass import getpass
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag



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


# Format for wrapped DEK
class WrappedDEK(TypedDict):
    ciphertext: bytes
    nonce: bytes
    policy_id: int


# Wrap DEK. Returns an encrypted DEK that can be stored in the vault.db
def wrap_dek(kek: bytes, dek: bytes, policy: "KDFPolicy") -> WrappedDEK:
    if len(kek) != 32:
        raise ValueError("KEK must be 32 bytes (AES-256).")
    if len(dek) != 32:
        raise ValueError("DEK must be 32 bytes.")

    nonce = os.urandom(12)
    aesgcm = AESGCM(kek)
    aad = f"policy:{policy.id}|kdfv:{policy.kdf_version}".encode("utf-8")

    ciphertext = aesgcm.encrypt(nonce=nonce, data=dek, associated_data=aad)

    return WrappedDEK(
        ciphertext=ciphertext,
        nonce=nonce,
        policy_id=policy.id,
    )


# Unwrap DEK. Returns the created DEK to encrypt new entries and decrypt existing entries in the vault_data table.
def unwrap_dek(kek: bytes, wrapped: WrappedDEK, policy: "KDFPolicy") -> bytes:
    if len(wrapped["nonce"]) != 12:
        raise ValueError("Invalid nonce length for AES-GCM (expected 12 bytes).")
    if len(wrapped["ciphertext"]) < 16:  # must at least contain the tag
        raise ValueError("Ciphertext too short to contain GCM tag.")

    aesgcm = AESGCM(kek)
    aad = f"policy:{policy.id}|kdfv:{policy.kdf_version}".encode("utf-8")

    try:
        return aesgcm.decrypt(
            nonce=wrapped["nonce"],
            data=wrapped["ciphertext"],
            associated_data=aad
        )
    except InvalidTag:
        raise ValueError("Unwrap failed: invalid tag (wrong key/nonce/AAD or corrupted data).")



# Generate new DEK. If no wrapped DEK is stored in the vault keys, a new DEK will be generated, wrapped and stored.
def generate_new_dek(session, kek: bytes, policy: "KDFPolicy"):
    dek = os.urandom(32)
    wrapped_dek = wrap_dek(kek=kek, dek=dek, policy=policy)

    vault_key = VaultKey(
        ciphertext=wrapped_dek['ciphertext'],
        nonce=wrapped_dek['nonce'],
        policy_id=wrapped_dek['policy_id'],
        active=True
    )

    session.add(vault_key)
    session.commit()
    

    return wrapped_dek






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

    # Obtain vault key (Obtain wrapped DEK row, or generate new DEK if not existant)
    existing_dek = session.query(VaultKey).filter_by(active=True).first()
    if existing_dek:
        wrapped_dek = WrappedDEK( 
            ciphertext=existing_dek.ciphertext, 
            nonce=existing_dek.nonce, 
            policy_id=existing_dek.policy_id, 
        )
    if not existing_dek:
        wrapped_dek = generate_new_dek(session=session, kek=kek, policy=policy)

    unwrapped_dek = unwrap_dek(kek=kek, wrapped=wrapped_dek, policy=policy)


if __name__ == "__main__":
    main()




