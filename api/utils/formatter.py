from traceback import format_exception
from typing import TypeVar, Type
from migrations.database.models.base import DeclarativeBase

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


def trim_extra_whitespaces(text: str) -> str:
    return " ".join(text.split())


def format_error(error: Exception) -> str:
    if not error:
        return ""
    lines = format_exception(type(error), error, error.__traceback__)
    return "\n".join(lines)


def format_models(raw: list[Type], model: Type[T]) -> list[T]:
    return [model.from_orm(elem) for elem in raw]
