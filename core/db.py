from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///vault.db", echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
Base = declarative_base()

def init_db():
    # Import models inside so their tables are registered on Base.metadata
    from core.models import KDFPolicy, VaultData, VaultKey
    Base.metadata.create_all(bind=engine)