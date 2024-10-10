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
