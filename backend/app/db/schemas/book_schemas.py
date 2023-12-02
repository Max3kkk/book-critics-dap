from datetime import datetime

from pydantic import BaseModel, Field, HttpUrl


class BookBase(BaseModel):
    review_hour_amount: int = Field(..., gt=0, lt=721)
    title: str = Field(..., min_length=5, max_length=100)
    description: str
    image_url: HttpUrl
    author_id: int = Field(..., gt=0)


class BookCreate(BookBase):
    pass

    class Config:
        orm_mode = True


class Book(BookBase):
    id: int
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True


class BookDetailed(BaseModel):
    title: str
    description: str
    image_url: HttpUrl
    author_full_name: str
    can_be_reviewed: bool
    hours_left: int
    minutes_left: int
