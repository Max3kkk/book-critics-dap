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

    class Config:
        orm_mode = True


class ReviewOut(ReviewBase):
    pass
