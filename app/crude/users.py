from fastapi import FastAPI, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User

async def get_all_users(db: AsyncSession) -> list[User]:
    """
    Fetch all users from the database.
    """    
    result = await db.execute(select(User))
    return result.scalars().all()

async def set_user(user_data: User, db: AsyncSession) -> User:
    """
    Create a new user in the database.
    """
    user = User(name=user_data.name, email=user_data.email)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user