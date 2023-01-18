import uuid
from datetime import datetime

from enum import Enum

from sqlalchemy import Column, String, TIMESTAMP, Boolean
from sqlalchemy.dialects.postgresql import UUID, ENUM
from pytz import UTC

from .base import DeclarativeBase


class CharacterTextDriver(str, Enum):
    SBER_GPT: str = "SBER_GPT"


class CharacterTTSDriver(str, Enum):
    GOOGLE_TTS: str = "GOOGLE_TTS"


class Characters(DeclarativeBase):
    __tablename__ = "characters"

    id = Column(UUID, unique=True, primary_key=True, default=lambda: str(uuid.uuid4()))
    is_active = Column(Boolean,nullable=False, default=False)
    name = Column(String, nullable=False)
    text_driver = Column(ENUM(CharacterTextDriver), nullable=False)
    tts_driver = Column(ENUM(CharacterTTSDriver), nullable=False)
    model_id = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default = lambda x: datetime.now(UTC))
