from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status
import typing as t

from app.db import models, schemas


def get_like(db: Session, user_id: int, review_id: int):
    return (
        db.query(models.Like)
        .filter(models.Like.user_id == user_id, models.Like.review_id == review_id)
        .first()
    )


def get_likes(db: Session, skip: int = 0, limit: int = 100) -> t.List[schemas.LikeOut]:
    return db.query(models.Like).offset(skip).limit(limit).all()


def create_like(db: Session, like: schemas.LikeCreate):
    # Check if the user exists
    user = db.query(models.User).filter(models.User.id == like.user_id).first()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    # Check if the review exists
    review = db.query(models.Review).filter(models.Review.id == like.review_id).first()
    if not review:
        raise HTTPException(status_code=400, detail="Review not found")

    db_like = models.Like(user_id=like.user_id, review_id=like.review_id)
    db.add(db_like)
    db.commit()
    return db_like


def delete_like(db: Session, user_id: int, review_id: int):
    like = get_like(db, user_id, review_id)
    if not like:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Like not found")
    db.delete(like)
    db.commit()
    return like
