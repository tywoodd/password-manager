from datetime import datetime
from sqlalchemy import Boolean, DateTime, Column, ForeignKey, Integer, LargeBinary, String
from sqlalchemy.orm import relationship
from db import Base


class KDFPolicy(Base):
    __tablename__ = 'kdf_policies'

    id = Column(Integer, primary_key=True)
    kdf = Column(String(32), nullable=False, default="argon2id")
    kdf_version = Column(Integer, nullable=False, default=1)
    hash_len = Column(Integer, nullable=False, default=32)
    cipher_name = Column(String(32), nullable=False, default="aes-256-gcm")
    cipher_nonce_len = Column(Integer, nullable=False, default=12)
    cipher_tag_len = Column(Integer, nullable=False, default=16)
    time_cost = Column(Integer, nullable=False, default=3)
    memory_cost = Column(Integer, nullable=False, default=65536)
    parallelism = Column(Integer, nullable=False, default=4)
    salt_b64 = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    singleton = Column(Integer, nullable=False, default=1, unique=True)

    vault_keys = relationship("VaultKey", back_populates="policy")


class VaultKey(Base):
    __tablename__ = "vault_keys"

    id = Column(Integer, primary_key=True)
    ciphertext = Column(LargeBinary, nullable=False)
    nonce = Column(LargeBinary, nullable=False)
    policy_id = Column(Integer, ForeignKey("kdf_policies.id"), nullable=False)
    active = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)

    policy = relationship("KDFPolicy", back_populates="vault_keys")


class VaultData(Base):
    __tablename__ = 'vault_data'

    id = Column(Integer, primary_key=True)
    entry_uuid = Column(String(36), unique=True, nullable=False)
    vault_key_id = Column(Integer, ForeignKey("vault_keys.id"), nullable=False)
    nonce = Column(LargeBinary, nullable=False)
    ciphertext = Column(LargeBinary, nullable=False)
    schema_v = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)