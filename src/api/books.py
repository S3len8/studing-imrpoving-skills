from typing import Annotated

from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from sqlalchemy import select

from src.api.dependencies import SessionDep
from src.database import Base, engine
from src.models.books import BookModel
from src.schemas.books import BookAddSchema

router = APIRouter()


@router.post("/setup_database")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {"ok": True}


@router.post("/books")
async def add_book(data: BookAddSchema, session: SessionDep):
    new_book = BookModel(
        title=data.title,
        author=data.author,
    )
    session.add(new_book)
    await session.commit()
    return {"ok": True}


class PaginationParams(BaseModel):
    limit: int = Field(5, ge=0, le=100, description="Кількість елементів для сторінки")
    offset: int = Field(0, ge=0, description="Зміщення для пагінації")


PaginationDep = Annotated[PaginationParams, Depends(PaginationParams)]


@router.get("/books")
async def get_books(session: SessionDep, pagination: PaginationDep) -> list[BookAddSchema]:
    query = select(BookModel).limit(pagination.limit).offset(pagination.offset)
    result = await session.execute(query)
    return result.scalars().all() 