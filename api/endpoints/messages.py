from uuid import UUID
from fastapi import APIRouter, Form, Body
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.ext.asyncio import AsyncSession

from migrations.database.connection.session import get_session
from api.utils.formatter import serialize_models
from api.schemas.common import SuccessfullResponse
from api.schemas.users import TelegramIdentity
from api.schemas.messages import Message, MessageGet, MessageCreate, MessageUpdate
from api.services.messages import get_user_messages, add_new_message, update_message

messages_router = APIRouter(tags=["Character functionality"])


# TODO: move this functionality to another service

@messages_router.get("/user/messages", response_model=list[Message])
async def get_dialog_messages(
    message_get: MessageGet = Depends(),
    identity: TelegramIdentity = Depends(),
    session: AsyncSession = Depends(get_session)
) -> list[Message]:
    messages = await get_user_messages(message_get, identity, session)
    return serialize_models(messages, Message)


@messages_router.post("/user/message", response_model=SuccessfullResponse)
async def create_dialog_message(
    message_create: MessageCreate = Depends(),
    identity: TelegramIdentity = Depends(),
    session: AsyncSession = Depends(get_session)
) -> SuccessfullResponse:
    await add_new_message(message_create, identity, session)
    return SuccessfullResponse()


@messages_router.put("/user/message", response_model=SuccessfullResponse)
async def update_dialog_message(
    message_update: MessageUpdate = Depends(),
    identity: TelegramIdentity = Depends(),
    session: AsyncSession = Depends(get_session)
) -> SuccessfullResponse:
    await update_message(message_update, identity, session)
    return SuccessfullResponse()
