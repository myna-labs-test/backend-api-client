from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field
from migration.database.models.messages import SenderTypes


class Message(BaseModel):
    id: UUID = Field(..., description='Message UUID')
    message: str = Field(..., description='Message text')
    sender_type: SenderTypes = Field(..., description='Sender type')

    class Config:
        orm_mode: bool = True


class MessageGet(BaseModel):
    character_id: UUID = Field(..., description='Character UUID')


class MessageCreate(BaseModel):
    sender_type: SenderTypes = Field(..., description='Sender type')
    message: str = Field(..., description='Message text')
    character_id: UUID = Field(..., description='Character UUID')


class MessageUpdate(BaseModel):
    id: UUID = Field(..., description='Message id')
    message: str = Field(..., description='New message text')
