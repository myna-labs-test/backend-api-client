import uuid
from datetime import datetime

from enum import Enum

from sqlalchemy import Column, String, TIMESTAMP, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, ENUM
from .characters import Characters
from pytz import UTC

from .base import DeclarativeBase


class Users(DeclarativeBase):
    __tablename__ = "users"

    id = Column(UUID, unique=True, primary_key=True, default=lambda: str(uuid.uuid4()))
    tg_id = Column(Integer, unique=True, nullable=False, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String, unique=True, nullable=False, primary_key=True)
    active_character_id = Column(UUID, ForeignKey(Characters.id, ondelete="CASCADE"), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default = lambda x: datetime.now(UTC))

