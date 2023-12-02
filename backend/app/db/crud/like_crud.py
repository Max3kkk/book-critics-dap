from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status
import typing as t

from app.db import models, schemas
from db.crud.book_crud import book_in_review_time


def get_like(db: Session, user_id: int, review_id: int):
    return (
        db.query(models.Like)
        .filter(models.Like.user_id == user_id, models.Like.review_id == review_id)
        .first()
    )


def create_like(
    db: Session,
    user_id,
    review_id: int,
):
    review = db.query(models.Review).filter(models.Review.id == review_id).first()
    if not review:
        raise HTTPException(status_code=400, detail="Review not found")
    if not book_in_review_time(review.book.created_at, review.book.review_hour_amount):
        raise HTTPException(
            status_code=400, detail="The book review is over, you cannot like it"
        )
    db_like = models.Like(user_id=user_id, review_id=review_id)
    db.add(db_like)
    db.commit()
    return db_like


def delete_like(db: Session, user_id: int, review_id: int):
    like = get_like(db, user_id, review_id)
    if not like:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Like not found")
    if not book_in_review_time(
        like.review.book.created_at, like.review.book.review_hour_amount
    ):
        raise HTTPException(
            status_code=400, detail="The book review is over, you cannot like it"
        )
    db.delete(like)
    db.commit()
    return like
