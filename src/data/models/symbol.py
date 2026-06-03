# Provides a place to create our tables using sqlalchemy ORM
from __future__ import annotations

from datetime import UTC, datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base


class Symbol(Base):
    __tablename__ = 'symbol'

    # primary_key=True => autoincrement
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    ticker: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    exchange: Mapped[str] = mapped_column(String(10), nullable=True, default=None)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(UTC))




