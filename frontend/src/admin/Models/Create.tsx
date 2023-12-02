import React, { FC } from 'react';
import {
  Create,
  SimpleForm,
  TextInput,
  PasswordInput,
  BooleanInput,
} from 'react-admin';

// class User(Base):
//     __tablename__ = "user"

//     id = Column(Integer, primary_key=True, index=True)
//     email = Column(String, unique=True, index=True, nullable=False)
//     first_name = Column(String)
//     last_name = Column(String)
//     hashed_password = Column(String, nullable=False)
//     is_superuser = Column(Boolean, default=False)

//     reviews = relationship("Review", back_populates="user_created")


// class Author(Base):
//     __tablename__ = "author"

//     id = Column(Integer, primary_key=True, index=True)
//     full_name = Column(String, nullable=False)

//     books = relationship("Book", back_populates="author")


// class Book(Base):
//     __tablename__ = "book"

//     id = Column(Integer, primary_key=True, index=True)
//     title = Column(String, nullable=False)
//     description = Column(String, nullable=False)
//     image_url = Column(String, nullable=False)
//     author_id = Column(Integer, ForeignKey("author.id"))

//     author = relationship("Author", back_populates="books")
//     reviews = relationship("Review", back_populates="book")


// class Review(Base):
//     __tablename__ = "review"

//     id = Column(Integer, primary_key=True, index=True)
//     text = Column(String, nullable=False)
//     user_created_id = Column(Integer, ForeignKey("user.id"))
//     book_id = Column(Integer, ForeignKey("book.id"))

//     book = relationship("Book", back_populates="reviews")
//     user_created = relationship("User", back_populates="reviews")
//     likes = relationship("Like", back_populates="review")
//     dislikes = relationship("Dislike", back_populates="review")


// class Like(Base):
//     __tablename__ = "like"

//     user_id = Column(Integer, ForeignKey("user.id"))
//     review_id = Column(Integer, ForeignKey("review.id"))

//     review = relationship("Review", back_populates="likes")

//     __table_args__ = (PrimaryKeyConstraint("user_id", "review_id"),)


// class Dislike(Base):
//     __tablename__ = "dislike"

//     user_id = Column(Integer, ForeignKey("user.id"))
//     review_id = Column(Integer, ForeignKey("review.id"))

//     review = relationship("Review", back_populates="dislikes")

//     __table_args__ = (PrimaryKeyConstraint("user_id", "review_id"),)


export const UserCreate: FC = (props) => (
  <Create {...props}>
    <SimpleForm>
      <TextInput source="email" />
      <TextInput source="first_name" />
      <TextInput source="last_name" />
      <PasswordInput source="password" />
      <BooleanInput source="is_superuser" />
    </SimpleForm>
  </Create>
);

export const AuthorCreate: FC = (props) => (
  <Create {...props}>
    <SimpleForm>
      <TextInput source="full_name" />
    </SimpleForm>
  </Create>
);

export const BookCreate: FC = (props) => (
  <Create {...props}>
    <SimpleForm>
      <TextInput source="title" />
      <TextInput source="description" />
      <TextInput source="image_url" />
      <TextInput source="author_id" />
    </SimpleForm>
  </Create>
);

export const ReviewCreate: FC = (props) => (
  <Create {...props}>
    <SimpleForm>
      <TextInput source="text" />
      <TextInput source="user_created_id" />
      <TextInput source="book_id" />
    </SimpleForm>
  </Create>
);

export const LikeCreate: FC = (props) => (
  <Create {...props}>
    <SimpleForm>
      <TextInput source="user_id" />
      <TextInput source="review_id" />
    </SimpleForm>
  </Create>
);

export const DislikeCreate: FC = (props) => (
  <Create {...props}>
    <SimpleForm>
      <TextInput source="user_id" />
      <TextInput source="review_id" />
    </SimpleForm>
  </Create>
);