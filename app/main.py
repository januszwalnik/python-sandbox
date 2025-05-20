'''
FastAPI imports
'''
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import random
import asyncio
from faker import Faker
'''
Internal imports
'''
from app.crude.users import get_all_users, set_user
from app.db.database import get_db
from app.models.user import User
from app.schemas.user import User_Create, User_Base

import uvicorn

'''
Redis imports
'''
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
import redis.asyncio as redis

app = FastAPI()

pod_name = Faker().first_name()

@app.on_event("startup")
"""
Event handler for FastAPI application startup.

Initializes the Redis client and sets up FastAPICache with a Redis backend.
Raises a RuntimeError if the cache falls back to the in-memory backend,
indicating that Redis was not properly initialized.
"""
async def on_startup():
    global redis_client
    redis_client = redis.from_url("redis://localhost:6379", encoding="utf8", decode_responses=False)
    FastAPICache.init(RedisBackend(redis_client), prefix="fastapi-cache")
    backend = FastAPICache.get_backend()
    if backend.__class__.__name__ == "InMemoryBackend":
        raise RuntimeError("Fallback cache is active! Redis not initialized.")
    
    

@app.get("/user", response_model=list[User_Base])
async def get_users(db: AsyncSession = Depends(get_db)):
    """
        Endpoint to retrieve a list of all users.

        This asynchronous endpoint fetches all users from the database, with the results cached for 60 seconds under the "user_all" namespace.
        A simulated delay of 4 seconds is introduced before fetching the users.

        Args:
            db (AsyncSession): The asynchronous database session dependency.

        Returns:
            list[User_Base]: A list of user objects conforming to the User_Base schema.
    """
    async def fetch_users():
        await asyncio.sleep(4)
        return await get_all_users(db)
    return await cache(expire=60, namespace="user_all")(fetch_users)()

@app.post("/user/", response_model=User_Base)
async def create_user(user: User_Create, db: AsyncSession = Depends(get_db)):
    """
    Asynchronously creates a new user in the database.
    Args:
        user (User_Create): The user data to create a new user.
        db (AsyncSession, optional): The asynchronous database session. Defaults to Depends(get_db).
    Returns:
        The result of the user creation operation.
    Side Effects:
        Clears the FastAPICache for the "user_all" namespace after creating the user.
    """
    result = await set_user(user, db)
    await FastAPICache.clear(namespace="user_all")
    return result

@app.get("/pod-name")
def get_pod_name():
    """
    Retrieve the name of the current pod.
    Returns:
        dict: A dictionary containing the pod name with the key 'pod_name'.
    """
    
    return {"pod_name": pod_name}


@app.get("/clear-cache")
async def cleare_cache_endpoint() -> dict:
    """
    Asynchronously clears the FastAPI cache.
    This endpoint clears all cached data managed by FastAPICache and returns a confirmation message.
    Returns:
        dict: A message indicating that the cache has been cleared.
    """
    await FastAPICache.clear()
    return {"message": "Cache cleared"}

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()