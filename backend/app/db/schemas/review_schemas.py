from datetime import datetime

from pydantic import BaseModel, Field


class ReviewBase(BaseModel):
    text: str
    user_created_id: int = Field(..., gt=0)
    book_id: int = Field(..., gt=0)


class ReviewCreate(ReviewBase):
    pass

    class Config:
        orm_mode = True


class Review(ReviewBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class BookReview(BaseModel):
    text: str
    user_email: str
    like_amount: int
    dislike_amount: int
    created_by_current_user: bool = False
