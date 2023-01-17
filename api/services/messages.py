
from migrations.database.models import Messages, Users
from migrations.database.models.messages import SenderTypes
from api.exceptions.common import BadRequest, NotFoundException, InternalServerError

from api.schemas.users import UserRegister, TelegramIdentity
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, and_, or_, update
from sqlalchemy.exc import IntegrityError
from api.schemas.users import TelegramIdentity
from api.schemas.messages import MessageGet, MessageUpdate, MessageCreate
from sqlalchemy.util._collections import immutabledict


async def get_user_messages(message_get: MessageGet, identity: TelegramIdentity, session: AsyncSession) -> list[Messages]:
    try:
        query = select(Messages).join(Users, Messages.user_id == Users.id).where(
            and_(
                Users.tg_id == identity.tg_id,
                Messages.character_id == str(message_get.character_id),
            )
        )
        messages = (await session.execute(query)).scalars().all()
        return messages
    except IntegrityError as e:
        raise InternalServerError(e) from e


async def add_new_message(message_create: MessageCreate, identity: TelegramIdentity, session: AsyncSession) -> None:
    try:
        query = insert(Messages).values(
            message=message_create.message,
            sender_type=message_create.sender_type,
            user_id=select(Users.id).where(
                  Users.tg_id == identity.tg_id
            ),
            character_id=str(message_create.character_id),
        )
        await session.execute(query)
        await session.commit()
    except IntegrityError as e:
        raise InternalServerError(e) from e


async def update_message(message_update: MessageUpdate, identity: TelegramIdentity, session: AsyncSession) -> None:
    try:
        query = update(Messages).values(
            message=message_update.message,
        ).where(
            and_(
                Messages.id == str(message_update.id),
                Messages.user_id.in_(select(Users.id).where(
                    Users.tg_id == identity.tg_id
                ))
            )
        )
        await session.execute(query, execution_options=immutabledict({"synchronize_session": 'fetch'}))
        await session.commit()
    except IntegrityError as e:
        raise InternalServerError(e) from e
