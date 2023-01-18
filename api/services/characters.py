from uuid import UUID
from migrations.database.models import Characters

from api.exceptions.common import BadRequest, NotFoundException, InternalServerError

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, and_, or_
from sqlalchemy.exc import IntegrityError


async def get_available_characters(session: AsyncSession) -> list[Characters]:
    query = select(Characters).where(
        Characters.is_active==True
    )
    characters = (await session.execute(query)).scalars().all()
    return characters


async def get_character(character_id: UUID, session: AsyncSession) -> Characters:
    query = select(Characters).where(
        Characters.id == str(character_id)
    )
    character = (await session.execute(query)).scalars().first()
    if not character:
        raise NotFoundException("Character not found")
    return character
