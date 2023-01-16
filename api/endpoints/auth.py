from uuid import UUID
from fastapi import APIRouter, Form, Body
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.ext.asyncio import AsyncSession

from api.exceptions.common import ForbiddenException
from api.schemas.common import SuccessfullResponse
from migrations.database.connection.session import get_session
from api.services.auth import add_new_user
from api.schemas.auth import UserRegister


auth_router = APIRouter(tags=["User authentication"])
# TODO: update метод


@auth_router.post("/user/register", response_model=SuccessfullResponse)
async def user_register(
    user_register: UserRegister = Depends(),
    session: AsyncSession = Depends(get_session)
) -> SuccessfullResponse:
    await add_new_user(user_register, session)
    return SuccessfullResponse()
