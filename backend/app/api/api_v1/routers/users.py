import typing as t

from fastapi import APIRouter, Depends, Response, HTTPException

from app.core.auth import get_current_active_user, get_current_active_superuser
from app.db.crud import (
    get_users,
    get_user,
    create_user,
    delete_user,
    edit_user,
)
from app.db.schemas import UserCreate, UserEdit, User
from app.db.session import get_db

users_router = r = APIRouter()


@r.get(
    "/users",
    response_model=t.List[User],
    response_model_exclude_none=True,
)
async def users_list(
    response: Response,
    db=Depends(get_db),
):
    """
    Get all users
    """
    users = get_users(db)
    response.headers["Content-Range"] = f"0-9/{len(users)}"
    return users


@r.get("/users/me", response_model=User, response_model_exclude_none=True)
async def user_me(current_user=Depends(get_current_active_user)):
    """
    Get own user
    """
    return current_user


@r.get(
    "/users/{user_id}",
    response_model=User,
    response_model_exclude_none=True,
)
async def user_details(
    user_id: int,
    db=Depends(get_db),
):
    """
    Get any user details
    """
    user = get_user(db, user_id)
    return user
    # return encoders.jsonable_encoder(
    #     user, skip_defaults=True, exclude_none=True,
    # )


@r.post("/users", response_model=User, response_model_exclude_none=True)
async def user_create(
    user: UserCreate,
    db=Depends(get_db),
):
    """
    Create a new user
    """
    return create_user(db, user)


@r.put("/users/{user_id}", response_model=User, response_model_exclude_none=True)
async def user_edit(
    user_id: int,
    user: UserEdit,
    db=Depends(get_db),
):
    """
    Update existing user
    """
    return edit_user(db, user_id, user)


@r.delete("/users/{user_id}", response_model=User, response_model_exclude_none=True)
async def user_delete(
    user_id: int,
    db=Depends(get_db),
    current_user=Depends(get_current_active_superuser),
):
    """
    Delete existing user
    """
    if current_user.id == user_id:
        raise HTTPException(
            status_code=400,
            detail="You cannot delete yourself",
        )
    return delete_user(db, user_id)
