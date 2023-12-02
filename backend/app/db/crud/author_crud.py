from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.db import models, schemas


def get_author(db: Session, author_id: int):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


def get_authors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Author).offset(skip).limit(limit).all()


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(full_name=author.full_name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def delete_author(db: Session, author_id: int):
    author = get_author(db, author_id)
    if not author:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Author not found")

    db.delete(author)
    db.commit()
    return author


def edit_author(
    db: Session, author_id: int, author: schemas.AuthorCreate
) -> schemas.Author:
    db_author = get_author(db, author_id)
    if not db_author:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Author not found")
    update_data = author.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_author, key, value)

    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author
