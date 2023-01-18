import uuid
from datetime import datetime

from enum import Enum

from sqlalchemy import Column, String, TIMESTAMP, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID, ENUM
from pytz import UTC

from .base import DeclarativeBase
from .users import Users
from .characters import Characters


class SenderTypes(str, Enum):
    USER: str = "USER"
    CHARACTER: str = "CHARACTER"


class Messages(DeclarativeBase):
    __tablename__ = "messages"

    id = Column(UUID, unique=True, primary_key=True, default=lambda: str(uuid.uuid4()))
    message = Column(String, nullable=False, index=True)
    sender_type = Column(ENUM(SenderTypes), nullable=False)
    user_id = Column(UUID, ForeignKey(Users.id, ondelete="CASCADE"), nullable=False)
    character_id = Column(UUID, ForeignKey(Characters.id, ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default = lambda x: datetime.now(UTC))

