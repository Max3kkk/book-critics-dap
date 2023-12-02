from pydantic import BaseModel


class LikeBase(BaseModel):
    user_id: int
    review_id: int


class LikeCreate(LikeBase):
    pass

    class Config:
        orm_mode = True


class Like(LikeBase):
    pass

    class Config:
        orm_mode = True


class LikeOut(LikeBase):
    pass


class DislikeBase(BaseModel):
    user_id: int
    review_id: int


class DislikeCreate(DislikeBase):
    pass

    class Config:
        orm_mode = True


class Dislike(DislikeBase):
    pass

    class Config:
        orm_mode = True


class DislikeOut(DislikeBase):
    pass
