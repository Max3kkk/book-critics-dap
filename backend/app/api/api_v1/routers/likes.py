from fastapi import APIRouter, Depends, Response, HTTPException
from starlette import status

from app.db.crud.like_crud import (
    get_likes,
    create_like,
    delete_like,
    get_like,
)
from app.db.schemas.like_schemas import Like, LikeCreate
from app.db.session import get_db

import typing as t

from db.crud.dislike_crud import get_dislike, delete_dislike

like_router = r = APIRouter()


@r.get("", response_model=t.List[Like], response_model_exclude_none=True)
async def likes_list(response: Response, db=Depends(get_db)):
    likes = get_likes(db)
    response.headers["Content-Range"] = f"0-9/{len(likes)}"
    return likes


@r.post("", response_model=Like, response_model_exclude_none=True)
async def like_create(like: LikeCreate, db=Depends(get_db)):
    review_id = like.review_id
    user_id = like.user_id
    if get_dislike(db, user_id, review_id):
        delete_dislike(db, user_id, review_id)
    if db_like := get_like(db, user_id, review_id):
        return db_like
    return create_like(db, like)


@r.get("/{user_id}/{review_id}", response_model=Like, response_model_exclude_none=True)
async def like_details(user_id: int, review_id: int, db=Depends(get_db)):
    if not get_dislike(db, user_id, review_id):
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Like not found")
    return get_like(db, user_id, review_id)


@r.delete(
    "/{user_id}/{review_id}", response_model=Like, response_model_exclude_none=True
)
async def like_delete(user_id: int, review_id: int, db=Depends(get_db)):
    return delete_like(db, user_id, review_id)
