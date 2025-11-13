from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from app.models import Base

load_dotenv(".env.development")

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL not set")

# Create the SQLAlchemy engine (connection to Postgres)
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Factory for DB sessions (used per-request in FastAPI)
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)
