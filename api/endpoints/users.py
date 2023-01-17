from uuid import UUID
from fastapi import APIRouter, Form, Body
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.ext.asyncio import AsyncSession

from api.exceptions.common import ForbiddenException
from api.schemas.common import SuccessfullResponse
from migrations.database.connection.session import get_session
from api.services.users import add_new_user, set_active_character, get_tg_user_by_identity
from api.schemas.users import UserRegister, ChooseCharacter, ActiveCharacter, TelegramIdentity


users_router = APIRouter(tags=["User authentication"])
# TODO: update метод


@users_router.post("/user/register", response_model=SuccessfullResponse)
async def user_register(
    user_register: UserRegister = Depends(),
    session: AsyncSession = Depends(get_session)
) -> SuccessfullResponse:
    await add_new_user(user_register, session)
    return SuccessfullResponse()


@users_router.put("/user/character", response_model=SuccessfullResponse)
async def user_register(
    choose_character: ChooseCharacter = Depends(),
    identity: TelegramIdentity = Depends(),
    session: AsyncSession = Depends(get_session)
) -> SuccessfullResponse:
    await set_active_character(choose_character, identity, session)
    return SuccessfullResponse()


@users_router.get("/user/character", response_model=ActiveCharacter)
async def user_register(
    identity: TelegramIdentity = Depends(),
    session: AsyncSession = Depends(get_session)
) -> ActiveCharacter:
    user = await get_tg_user_by_identity(identity, session)
    return ActiveCharacter(character_id=user.active_character_id)