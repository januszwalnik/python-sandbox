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
async def on_startup():
    global redis_client
    redis_client = redis.from_url("redis://localhost:6379", encoding="utf8", decode_responses=False)
    FastAPICache.init(RedisBackend(redis_client), prefix="fastapi-cache")
    backend = FastAPICache.get_backend()
    if backend.__class__.__name__ == "InMemoryBackend":
        raise RuntimeError("Fallback cache is active! Redis not initialized.")
    

@app.get("/user", response_model=list[User_Base])
async def get_users(db: AsyncSession = Depends(get_db)):
    async def fetch_users():
        await asyncio.sleep(4)
        return await get_all_users(db)
    return await cache(expire=60, namespace="user_all")(fetch_users)()

@app.post("/user/", response_model=User_Base)
async def create_user(user: User_Create, db: AsyncSession = Depends(get_db)):
    result = await set_user(user, db)
    await FastAPICache.clear(namespace="user_all")
    return result

@app.get("/pod-name")
def get_pod_name():
    return {"pod_name": pod_name}


@app.get("/clear-cache")
async def cleare_cache_endpoint():
    """
    This endpoint clears the cache from the redis entirely, which means that all of the keys will be removed.
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