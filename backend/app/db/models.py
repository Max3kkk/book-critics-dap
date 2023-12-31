from datetime import datetime

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Boolean,
    PrimaryKeyConstraint,
    Text,
    DateTime,
)
from sqlalchemy.orm import relationship

from .session import Base


def cascade_relationship(*args, **kwargs):
    kwargs.setdefault("cascade", "all, delete")
    return relationship(*args, **kwargs)


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String, nullable=False)
    is_superuser = Column(Boolean, default=False)

    reviews = cascade_relationship("Review", back_populates="user_created")


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)

    books = cascade_relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    image_url = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    author_id = Column(Integer, ForeignKey("author.id"))
    review_hour_amount = Column(Integer, nullable=False)

    author = relationship("Author", back_populates="books")
    reviews = cascade_relationship("Review", back_populates="book")


class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    user_created_id = Column(Integer, ForeignKey("user.id"))
    book_id = Column(Integer, ForeignKey("book.id"))

    book = relationship("Book", back_populates="reviews")
    user_created = relationship("User", back_populates="reviews")
    likes = cascade_relationship("Like", back_populates="review")
    dislikes = cascade_relationship("Dislike", back_populates="review")


class Like(Base):
    __tablename__ = "like"

    user_id = Column(Integer, ForeignKey("user.id"))
    review_id = Column(Integer, ForeignKey("review.id"))

    review = relationship("Review", back_populates="likes")

    __table_args__ = (PrimaryKeyConstraint("user_id", "review_id"),)


class Dislike(Base):
    __tablename__ = "dislike"

    user_id = Column(Integer, ForeignKey("user.id"))
    review_id = Column(Integer, ForeignKey("review.id"))

    review = relationship("Review", back_populates="dislikes")

    __table_args__ = (PrimaryKeyConstraint("user_id", "review_id"),)
