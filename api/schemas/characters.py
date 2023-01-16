from uuid import UUID
from pydantic import BaseModel, Field


class Character(BaseModel):
    id: UUID = Field(..., description='Character uuid')
    name: str = Field(..., description='Character name')

    class Config:
        orm_mode: bool = True
