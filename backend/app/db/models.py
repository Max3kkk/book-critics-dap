from sqlalchemy import Boolean, Column, Integer, String

from .session import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String, nullable=False)
    is_superuser = Column(Boolean, default=False)

    reviews = relationship("Review", back_populates="user_created")


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)

    books = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    image_url = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("author.id"))

    author = relationship("Author", back_populates="books")
    reviews = relationship("Review", back_populates="book")


class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    user_created_id = Column(Integer, ForeignKey("user.id"))
    book_id = Column(Integer, ForeignKey("book.id"))

    book = relationship("Book", back_populates="reviews")
    user_created = relationship("User", back_populates="reviews")
    likes = relationship("Like", back_populates="review")
    dislikes = relationship("Dislike", back_populates="review")


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
