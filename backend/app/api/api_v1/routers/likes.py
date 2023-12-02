from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from app.db.crud.like_crud import (
    create_like,
    delete_like,
    get_like,
)
from app.db.schemas.like_schemas import Like, LikeCreate
from app.db.session import get_db
from core.auth import get_current_active_user
from db.crud.dislike_crud import get_dislike, delete_dislike
from db.models import User

like_router = r = APIRouter()


@r.post("/{review_id}", response_model=Like, response_model_exclude_none=True)
async def like_create(
    review_id: int,
    db=Depends(get_db),
    user: User = Depends(get_current_active_user),
):
    user_id = user.id
    if get_dislike(db, user_id, review_id):
        delete_like(db, user_id, review_id)
    if existing_like := get_like(db, user_id, review_id):
        return existing_like
    return create_like(db, user_id, review_id)


@r.delete("/{review_id}", response_model=Like, response_model_exclude_none=True)
async def like_delete(
    review_id: int,
    user: User = Depends(get_current_active_user),
    db=Depends(get_db),
):
    user_id = user.id
    if not get_like(db, user_id, review_id):
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Like not found")
    return delete_like(db, user_id, review_id)
