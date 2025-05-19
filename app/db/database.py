from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

from fastapi import Depends

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

USER="fastapi_user"
PASSWORD="fastapi_pass"
DATABASE="fastapi_db"
HOST="localhost"
PORT=5432

DATABASE_URL = f"postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}/{DATABASE}"

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
        
