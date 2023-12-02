import typing as t

from fastapi import APIRouter, Depends, Response

from app.db.crud.review_crud import (
    get_reviews,
    create_review,
    edit_review,
    delete_review,
    get_review,
    get_book_review_list,
)
from app.db.schemas.review_schemas import Review, ReviewCreate, BookReview
from app.db.session import get_db
from core.auth import get_current_active_user

review_router = r = APIRouter()


@r.get("", response_model=t.List[Review], response_model_exclude_none=True)
async def reviews_list(response: Response, db=Depends(get_db)):
    reviews = get_reviews(db)
    response.headers["Content-Range"] = f"0-9/{len(reviews)}"
    return reviews


@r.get("/{review_id}", response_model=Review, response_model_exclude_none=True)
async def review_details(review_id: int, db=Depends(get_db)):
    return get_review(db, review_id)


@r.get(
    "/book/{book_id}",
    response_model=t.List[BookReview],
    response_model_exclude_none=True,
)
async def get_book_reviews(
    book_id: int,
    response: Response,
    db=Depends(get_db),
    user=Depends(get_current_active_user),
):
    book_reviews = get_book_review_list(db, book_id, user.id)
    response.headers["Content-Range"] = f"0-9/{len(book_reviews)}"
    return book_reviews


@r.post("", response_model=Review, response_model_exclude_none=True)
async def review_create(
    review: ReviewCreate, db=Depends(get_db), user=Depends(get_current_active_user)
):
    return create_review(db, review, user.id)


@r.put("/{review_id}", response_model=Review, response_model_exclude_none=True)
async def review_edit(review_id: int, review: ReviewCreate, db=Depends(get_db)):
    return edit_review(db, review_id, review)


@r.delete("/{review_id}", response_model=Review, response_model_exclude_none=True)
async def review_delete(review_id: int, db=Depends(get_db)):
    return delete_review(db, review_id)
