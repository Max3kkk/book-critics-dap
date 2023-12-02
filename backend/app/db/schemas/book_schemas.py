from pydantic import BaseModel, Field, HttpUrl


class BookBase(BaseModel):
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

    class Config:
        orm_mode = True


class BookOut(BookBase):
    pass
