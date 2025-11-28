from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

from fastapi import Depends

from sqlalchemy.ext.declarative import declarative_base

# Pull variables from .env file
import os
from dotenv import load_dotenv

Base = declarative_base()

try:
    load_dotenv()
except Exception:
    pass

USER = os.getenv("DB_USER", "fastapi_user")
PASSWORD = os.getenv("DB_PASSWORD", "fastapi_pass")
DATABASE = os.getenv("DATABASE", "fastapi_db")
HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", "5432"))

DATABASE_URL = f"postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}/{DATABASE}"

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
        
