from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status
import typing as t

from app.db import models, schemas


def get_review(db: Session, review_id: int):
    review = db.query(models.Review).filter(models.Review.id == review_id).first()
    if not review:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Review not found")
    return review


def get_reviews(
    db: Session, skip: int = 0, limit: int = 100
) -> t.List[schemas.ReviewOut]:
    return db.query(models.Review).offset(skip).limit(limit).all()


def create_review(db: Session, review: schemas.ReviewCreate):
    # Check if the user exists
    user = (
        db.query(models.User).filter(models.User.id == review.user_created_id).first()
    )
    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    # Check if the book exists
    book = db.query(models.Book).filter(models.Book.id == review.book_id).first()
    if not book:
        raise HTTPException(status_code=400, detail="Book not found")

    db_review = models.Review(
        text=review.text, user_created_id=review.user_created_id, book_id=review.book_id
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


def edit_review(
    db: Session, review_id: int, review: schemas.ReviewCreate
) -> schemas.Review:
    db_review = get_review(db, review_id)
    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")

    # Check if the user exists
    if review.user_created_id is not None:
        user = (
            db.query(models.User)
            .filter(models.User.id == review.user_created_id)
            .first()
        )
        if not user:
            raise HTTPException(status_code=400, detail="User not found")

    # Check if the book exists
    if review.book_id is not None:
        book = db.query(models.Book).filter(models.Book.id == review.book_id).first()
        if not book:
            raise HTTPException(status_code=400, detail="Book not found")

    update_data = review.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_review, key, value)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


def delete_review(db: Session, review_id: int):
    review = get_review(db, review_id)
    if not review:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Review not found")
    db.delete(review)
    db.commit()
    return review
