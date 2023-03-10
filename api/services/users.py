
from migration.database.models import Users

from api.exceptions.common import BadRequest, NotFoundException, InternalServerError

from api.schemas.users import UserRegister, TelegramIdentity, ChooseCharacter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, and_, or_, update
from sqlalchemy.exc import IntegrityError


async def add_new_user(user_register: UserRegister, session: AsyncSession) -> None:
    try:
        query = insert(Users).values(
            tg_id=user_register.tg_id,
            first_name=user_register.first_name,
            last_name=user_register.last_name,
            username=user_register.username
        )
        await session.execute(query)
        await session.commit()
    except IntegrityError as e:
        raise BadRequest("User already exist", e) from e


async def get_tg_user_by_identity(identity: TelegramIdentity, session: AsyncSession) -> Users:
    try:
        query = select(Users).where(
            Users.tg_id == identity.tg_id
        )
        user = (await session.execute(query)).scalars().first()
        if not user:
            raise NotFoundException("User not found")
        return user
    except IntegrityError as e:
        raise InternalServerError(e) from e


async def set_active_character(character: ChooseCharacter, identity: TelegramIdentity, session: AsyncSession) -> None:
    try:
        query = update(Users).values(
            active_character_id=str(character.character_id)
        ).where(
            Users.tg_id == identity.tg_id
        )
        await session.execute(query)
        await session.commit()
    except IntegrityError as e:
        raise NotFoundException('User or Character not found') from e
