from uuid import UUID
from pydantic import BaseModel, Field
from migrations.database.models.characters import CharacterTTSDriver, CharacterTextDriver


class Character(BaseModel):
    id: UUID = Field(..., description='Character UUID')
    name: str = Field(..., description='Character name')
    text_driver: CharacterTextDriver = Field(..., description='Character text driver')
    tts_driver: CharacterTTSDriver = Field(..., description='Character tts driver')
    model_id: str = Field(..., description='Character model id')

    class Config:
        orm_mode: bool = True


class CharacterChoose(BaseModel):
    character_id: UUID = Field(..., description='Character UUID')