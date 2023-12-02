from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from app.db.crud.dislike_crud import (
    create_dislike,
    delete_dislike,
    get_dislike,
)
from app.db.schemas import Dislike
from app.db.session import get_db
from core.auth import get_current_active_user
from db.crud.like_crud import get_like, delete_like
from db.models import User

dislike_router = r = APIRouter()


@r.post("/{review_id}", response_model=Dislike, response_model_exclude_none=True)
async def dislike_create(
    review_id: int,
    db=Depends(get_db),
    user: User = Depends(get_current_active_user),
):
    user_id = user.id
    if get_like(db, user_id, review_id):
        delete_like(db, user_id, review_id)
    if existing_dislike := get_dislike(db, user_id, review_id):
        return existing_dislike
    return create_dislike(db, user_id, review_id)


@r.delete("/{review_id}", response_model=Dislike, response_model_exclude_none=True)
async def dislike_delete(
    review_id: int,
    user: User = Depends(get_current_active_user),
    db=Depends(get_db),
):
    user_id = user.id
    if not get_dislike(db, user_id, review_id):
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Dislike not found")
    return delete_dislike(db, user_id, review_id)
