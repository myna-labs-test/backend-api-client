from uuid import UUID
from fastapi import APIRouter, Form, Body
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.ext.asyncio import AsyncSession

from migrations.database.connection.session import get_session
from api.schemas.characters import Character
from api.services.characters import get_available_characters
from api.utils.formatter import format_models

character_router = APIRouter(tags=["Character functionality"])


# TODO: move this functionality to another service

@character_router.get("/characters", response_model=list[Character])
async def get_user(
    session: AsyncSession = Depends(get_session)
) -> list[Character]:
    characters = await get_available_characters(session)
    return format_models(characters, Character)
