from pydantic import BaseModel, Field


class AuthorBase(BaseModel):
    full_name: str = Field(..., min_length=5, max_length=100)


class AuthorCreate(AuthorBase):
    pass

    class Config:
        orm_mode = True


class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True


class AuthorOut(AuthorBase):
    pass
