from uuid import UUID
from fastapi import Form
from pydantic import BaseModel, Field


class UserRegister(BaseModel):
    first_name: str = Form(..., description='Telegram user\'s first name')
    last_name: str = Form(..., description='Telegram user\'s last name')
    username: str = Form(..., description='Telegram username')
    tg_id: int = Form(..., description='Ссылка на Telegram пользователя')


class TelegramIdentity(BaseModel):
    tg_id: int = Field(..., title="Telegram user id", gt=0)


class ChooseCharacter(BaseModel):
    character_id: UUID = Field(..., description='Character UUID')


class ActiveCharacter(BaseModel):
    character_id: UUID = Field(None, description='Character UUID')
