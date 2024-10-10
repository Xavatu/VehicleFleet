import os

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "vehicle_fleet")
DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
async_engine = create_async_engine(DB_URL, echo=True)
async_session = async_sessionmaker(async_engine, expire_on_commit=False)


async def get_session():
    async with async_session() as session:
        yield session
