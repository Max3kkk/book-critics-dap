from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.db import models
from db.crud.book_crud import book_in_review_time


def get_dislike(db: Session, user_id: int, review_id: int):
    return (
        db.query(models.Dislike)
        .filter(
            models.Dislike.user_id == user_id, models.Dislike.review_id == review_id
        )
        .first()
    )


def create_dislike(db: Session, user_id: int, review_id: int):
    review = db.query(models.Review).filter(models.Review.id == review_id).first()
    if not review:
        raise HTTPException(status_code=400, detail="Review not found")

    if not book_in_review_time(review.book.created_at, review.book.review_hour_amount):
        raise HTTPException(
            status_code=400, detail="The book review is over, you cannot dislike it"
        )

    db_dislike = models.Dislike(user_id=user_id, review_id=review_id)
    db.add(db_dislike)
    db.commit()
    return db_dislike


def delete_dislike(db: Session, user_id: int, review_id: int):
    dislike = get_dislike(db, user_id, review_id)
    if not dislike:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Dislike not found")

    if not book_in_review_time(
        dislike.review.book.created_at, dislike.review.book.review_hour_amount
    ):
        raise HTTPException(
            status_code=400, detail="The book review is over, you cannot dislike it"
        )
    db.delete(dislike)
    db.commit()
    return dislike
