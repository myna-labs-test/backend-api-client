
from migrations.database.models import Characters

from api.exceptions.common import BadRequest, NotFoundException, InternalServerError

from api.schemas.auth import UserRegister, TelegramIdentity
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, and_, or_
from sqlalchemy.exc import IntegrityError


async def get_available_characters(session: AsyncSession) -> list[Characters]:
    try:
        query = select(Characters).where(
            Characters.is_active==True
        )
        characters = (await session.execute(query)).scalars().all()
        return characters
    except IntegrityError as e:
        raise InternalServerError(e) from e
