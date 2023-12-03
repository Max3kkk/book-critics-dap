import typing as t
from datetime import datetime, timedelta

from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.db import models, schemas
from db.models import User, Book


def get_book(db: Session, book_id: int):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


def get_detailed_book(db: Session, book_id: int, user: User) -> schemas.BookDetailed:
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    # Calculate the time left for the review
    end_time = book.created_at + timedelta(hours=book.review_hour_amount)
    time_left = end_time - datetime.now()

    hours_left = time_left.days * 24 + time_left.seconds // 3600
    minutes_left = (time_left.seconds // 60) % 60

    can_be_reviewed = book_can_be_reviewed(book, user.id)

    return schemas.BookDetailed(
        title=book.title,
        description=book.description,
        image_url=book.image_url,
        author_full_name=f"{book.author.full_name}",
        hours_left=hours_left,
        minutes_left=minutes_left,
        can_be_reviewed=can_be_reviewed,
    )


def book_can_be_reviewed(book: Book, user_id: int) -> bool:
    if user_id in book.reviews:
        raise HTTPException(status_code=400, detail="Book already reviewed")
    return book_in_review_time(book.created_at)


def book_in_review_time(created_at: datetime, review_hour_amount: int) -> bool:
    end_time = created_at + timedelta(hours=review_hour_amount)
    now = datetime.now()
    if now > end_time:
        return True
    return False


def get_books(db: Session, skip: int = 0, limit: int = 100) -> t.List[schemas.Book]:
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
        review_hour_amount=book.review_hour_amount,
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
