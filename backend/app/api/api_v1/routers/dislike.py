from fastapi import APIRouter, Depends, Response, HTTPException
from starlette import status

from app.db.crud.dislike_crud import (
    get_dislikes,
    create_dislike,
    delete_dislike,
    get_dislike,
)
from app.db.schemas import Dislike, DislikeCreate
from app.db.session import get_db

import typing as t

from db.crud.like_crud import get_like, delete_like

dislike_router = r = APIRouter()


@r.get("", response_model=t.List[Dislike], response_model_exclude_none=True)
async def dislikes_list(response: Response, db=Depends(get_db)):
    dislikes = get_dislikes(db)
    response.headers["Content-Range"] = f"0-9/{len(dislikes)}"
    return dislikes


@r.post("", response_model=Dislike, response_model_exclude_none=True)
async def dislike_create(dislike: DislikeCreate, db=Depends(get_db)):
    review_id = dislike.review_id
    user_id = dislike.user_id
    if get_like(db, user_id, review_id):
        delete_like(db, user_id, review_id)
    if existing_dislike := get_dislike(db, user_id, review_id):
        return existing_dislike
    return create_dislike(db, dislike)


@r.delete(
    "/{user_id}/{review_id}", response_model=Dislike, response_model_exclude_none=True
)
async def dislike_delete(user_id: int, review_id: int, db=Depends(get_db)):
    if not get_dislike(db, user_id, review_id):
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Dislike not found")
    return delete_dislike(db, user_id, review_id)


@r.get(
    "/{user_id}/{review_id}", response_model=Dislike, response_model_exclude_none=True
)
async def dislike_details(user_id: int, review_id: int, db=Depends(get_db)):
    return get_dislike(db, user_id, review_id)
