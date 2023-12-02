from fastapi import APIRouter, Depends, Response
from app.db.crud.book_crud import (
    get_books,
    create_book,
    edit_book,
    delete_book,
    get_book,
    get_detailed_book,
)
from app.db.schemas.book_schemas import Book, BookCreate, BookDetailed
from app.db.session import get_db
import typing as t

from core.auth import get_current_active_user

book_router = r = APIRouter()


@r.get("", response_model=t.List[Book], response_model_exclude_none=True)
async def books_list(response: Response, db=Depends(get_db)):
    books = get_books(db)
    response.headers["Content-Range"] = f"0-9/{len(books)}"
    return books


@r.get("/{book_id}", response_model=Book, response_model_exclude_none=True)
async def book_details(book_id: int, db=Depends(get_db)):
    return get_book(db, book_id)


@r.get(
    "detailed/{book_id}", response_model=BookDetailed, response_model_exclude_none=True
)
async def book_details_detailed(
    book_id: int, db=Depends(get_db), current_user=Depends(get_current_active_user)
):
    return get_detailed_book(db, book_id, current_user)


@r.post("", response_model=Book, response_model_exclude_none=True)
async def book_create(book: BookCreate, db=Depends(get_db)):
    return create_book(db, book)


@r.put("/{book_id}", response_model=Book, response_model_exclude_none=True)
async def book_edit(book_id: int, book: BookCreate, db=Depends(get_db)):
    return edit_book(db, book_id, book)


@r.delete("/{book_id}", response_model=Book, response_model_exclude_none=True)
async def book_delete(book_id: int, db=Depends(get_db)):
    return delete_book(db, book_id)
