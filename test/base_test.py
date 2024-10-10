import datetime
import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.config.base import Base
from app.models import Vehicle

TEST_DB_USER = "postgres"
TEST_DB_PASSWORD = "postgres"
TEST_DB_HOST = "localhost"
TEST_DB_PORT = "5432"
TEST_DB_NAME = "vehicle_fleet"
TEST_DB_URL = f"postgresql+asyncpg://{TEST_DB_USER}:{TEST_DB_PASSWORD}@{TEST_DB_HOST}:{TEST_DB_PORT}/{TEST_DB_NAME}"

async_engine = create_async_engine(TEST_DB_URL, echo=True)
async_session = async_sessionmaker(async_engine, expire_on_commit=False)


async def create_all():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def add_one():
    async with async_session() as session:
        session.add(
            Vehicle(
                id=0,
                production_year=0,
                mileage=0,
                cost=0,
                current_tax=0,
                registration_date=datetime.datetime.now(datetime.UTC),
            )
        )
        await session.commit()


async def get_one():
    async with async_session() as session:
        result = await session.get_one(Vehicle, ident=0)
        print(result)
        print(result.__dict__)


if __name__ == "__main__":
    """
    checking some new sqla 2.0 features
    """
    loop = asyncio.new_event_loop()
    loop.run_until_complete(create_all())
    loop.run_until_complete(add_one())
    loop.run_until_complete(get_one())
    loop.close()
