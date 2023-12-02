from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status
import typing as t

from app.db import models, schemas


def get_book(db: Session, book_id: int):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


def get_books(db: Session, skip: int = 0, limit: int = 100) -> t.List[schemas.BookOut]:
    return db.query(models.Book).offset(skip).limit(limit).all()


def delete_book(db: Session, book_id: int):
    book = get_book(db, book_id)
    if not book:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Book not found")
    db.delete(book)
    db.commit()
    return book


def create_book(db: Session, book: schemas.BookCreate):
    # Verify if the author exists
    author = db.query(models.Author).filter(models.Author.id == book.author_id).first()
    if not author:
        raise HTTPException(status_code=400, detail="Author not found")

    db_book = models.Book(
        title=book.title,
        description=book.description,
        image_url=book.image_url,
        author_id=book.author_id,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def edit_book(db: Session, book_id: int, book: schemas.BookCreate) -> schemas.Book:
    db_book = get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")

    # Verify if the author exists
    if book.author_id is not None:
        author = (
            db.query(models.Author).filter(models.Author.id == book.author_id).first()
        )
        if not author:
            raise HTTPException(status_code=400, detail="Author not found")

    update_data = book.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_book, key, value)

    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
