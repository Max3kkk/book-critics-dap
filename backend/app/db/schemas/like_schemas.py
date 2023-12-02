from pydantic import BaseModel


class LikeBase(BaseModel):
    review_id: int


class LikeCreate(LikeBase):
    pass

    class Config:
        orm_mode = True


class Like(LikeBase):
    user_id: int

    class Config:
        orm_mode = True


class DislikeBase(BaseModel):
    review_id: int


class DislikeCreate(DislikeBase):
    pass

    class Config:
        orm_mode = True


class Dislike(DislikeBase):
    user_id: int
    pass

    class Config:
        orm_mode = True
