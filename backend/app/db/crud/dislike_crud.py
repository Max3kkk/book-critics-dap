from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status
import typing as t

from app.db import models, schemas


def get_dislike(db: Session, user_id: int, review_id: int):
    return (
        db.query(models.Dislike)
        .filter(
            models.Dislike.user_id == user_id, models.Dislike.review_id == review_id
        )
        .first()
    )


def get_dislikes(
    db: Session, skip: int = 0, limit: int = 100
) -> t.List[schemas.DislikeOut]:
    return db.query(models.Dislike).offset(skip).limit(limit).all()


def create_dislike(db: Session, dislike: schemas.DislikeCreate):
    user = db.query(models.User).filter(models.User.id == dislike.user_id).first()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    # Check if the review exists
    review = (
        db.query(models.Review).filter(models.Review.id == dislike.review_id).first()
    )
    if not review:
        raise HTTPException(status_code=400, detail="Review not found")

    db_dislike = models.Dislike(user_id=dislike.user_id, review_id=dislike.review_id)
    db.add(db_dislike)
    db.commit()
    return db_dislike


def delete_dislike(db: Session, user_id: int, review_id: int):
    dislike = get_dislike(db, user_id, review_id)
    if not dislike:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Dislike not found")
    db.delete(dislike)
    db.commit()
    return dislike
