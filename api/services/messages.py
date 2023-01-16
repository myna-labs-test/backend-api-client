
from migrations.database.models import Messages, Users
from migrations.database.models.messages import MessageStatuses, SenderTypes
from api.exceptions.common import BadRequest, NotFoundException, InternalServerError

from api.schemas.auth import UserRegister, TelegramIdentity
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, and_, or_, update
from sqlalchemy.exc import IntegrityError
from api.schemas.auth import TelegramIdentity
from api.schemas.messages import MessageGet, MessageUpdate, MessageCreate


async def get_user_messages(message_get: MessageGet, identity: TelegramIdentity, session: AsyncSession) -> list[Messages]:
    try:
        query = select(Messages).join(Users, Messages.user_id == Users.id).where(
            and_(
                Users.tg_id == identity.tg_id,
                Messages.character_id == message_get.character_id,
                Messages.message_status == message_get.message_status
            )
        )
        messages = (await session.execute(query)).scalars().all()
        return messages
    except IntegrityError as e:
        raise InternalServerError(e) from e


async def add_new_message(message_create: MessageCreate, identity: TelegramIdentity, session: AsyncSession) -> None:
    message_status = MessageStatuses.NEED_PARSING if message_create.sender_type.value == SenderTypes.USER else MessageStatuses.NEED_SENDING
    try:
        query = insert(Messages).values(
            message=message_create.message,
            sender_type=message_create.sender_type,
            message_status=message_status,
            user_id=select(Users.id).where(
                  Users.tg_id == identity.tg_id
            ),
            character_id=message_create.character_id,
        )
        await session.execute(query)
        await session.commit()
    except IntegrityError as e:
        raise InternalServerError(e) from e


async def update_message(message_update: MessageUpdate, identity: TelegramIdentity, session: AsyncSession) -> None:
    try:
        query = update(Messages).values(
            message=message_update.message,
            message_status=message_update.message_status
        ).where(
            and_(
                Messages.id == message_update.id,
                Messages.user_id == select(Users).where(
                    Users.tg_id == identity.tg_id
                )
            )
        )
        await session.execute(query)
        await session.commit()
    except IntegrityError as e:
        raise InternalServerError(e) from e
