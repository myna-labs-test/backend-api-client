from uuid import UUID
from fastapi import APIRouter, Form, Body
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.ext.asyncio import AsyncSession

from migrations.database.connection.session import get_session
from api.schemas.characters import Character, CharacterChoose
from api.services.characters import get_available_characters, get_character
from api.utils.formatter import serialize_models

character_router = APIRouter(tags=["Character functionality"])


@character_router.get("/characters", response_model=list[Character])
async def get_characters(
    session: AsyncSession = Depends(get_session)
) -> list[Character]:
    characters = await get_available_characters(session)
    return serialize_models(characters, Character)


@character_router.get("/character", response_model=Character)
async def get_specific_character(
    character_choose: CharacterChoose = Depends(),
    session: AsyncSession = Depends(get_session)
) -> Character:
    character = await get_character(character_choose.character_id, session)
    return Character.from_orm(character)