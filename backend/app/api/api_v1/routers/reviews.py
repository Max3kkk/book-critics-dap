from fastapi import APIRouter, Depends, Response
from app.db.crud.review_crud import (
    get_reviews,
    create_review,
    edit_review,
    delete_review,
    get_review,
)
from app.db.schemas.review_schemas import Review, ReviewCreate
from app.db.session import get_db
import typing as t

review_router = r = APIRouter()


@r.get("", response_model=t.List[Review], response_model_exclude_none=True)
async def reviews_list(response: Response, db=Depends(get_db)):
    reviews = get_reviews(db)
    response.headers["Content-Range"] = f"0-9/{len(reviews)}"
    return reviews


@r.get("/{review_id}", response_model=Review, response_model_exclude_none=True)
async def review_details(review_id: int, db=Depends(get_db)):
    return get_review(db, review_id)


@r.post("", response_model=Review, response_model_exclude_none=True)
async def review_create(review: ReviewCreate, db=Depends(get_db)):
    return create_review(db, review)


@r.put("/{review_id}", response_model=Review, response_model_exclude_none=True)
async def review_edit(review_id: int, review: ReviewCreate, db=Depends(get_db)):
    return edit_review(db, review_id, review)


@r.delete("/{review_id}", response_model=Review, response_model_exclude_none=True)
async def review_delete(review_id: int, db=Depends(get_db)):
    return delete_review(db, review_id)
