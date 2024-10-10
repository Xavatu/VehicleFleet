import datetime
from typing import Optional

from sqlalchemy import (
    Identity,
    SmallInteger,
    BigInteger,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.config.base import Base
from app.mixins.sqla import TableNameMixin


class Vehicle(Base, TableNameMixin):
    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    production_year: Mapped[int] = mapped_column(SmallInteger, index=True)
    mileage: Mapped[int] = mapped_column(index=True)
    cost: Mapped[int] = mapped_column(BigInteger, index=True)
    registration_date: Mapped[datetime.datetime]
    current_tax: Mapped[Optional[int]]


if __name__ == "__main__":
    """
    checking some new sqla 2.0 features
    """
    import asyncio
    from app.config.db import async_engine, async_session

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

    loop = asyncio.new_event_loop()
    loop.run_until_complete(create_all())
    loop.run_until_complete(add_one())
    loop.run_until_complete(get_one())
    loop.close()
