import random

from faker import Faker

from app.db.crud import (
    create_user,
    create_author,
    create_book,
    create_review,
    create_like,
    create_dislike,
)
from app.db.schemas import (
    UserCreate,
    AuthorCreate,
    BookCreate,
    ReviewCreate,
)
from app.db.session import SessionLocal

fake = Faker()


def create_fake_data(
    db,
    num_users=10,
    num_authors=5,
    num_books=15,
    num_reviews=30,
    num_likes=50,
    num_dislikes=20,
):
    # Create admin user
    create_user(
        db, UserCreate(email="admin@admin.com", password="admin", is_superuser=True)
    )
    # Create users
    for _ in range(num_users):
        create_user(
            db,
            UserCreate(
                email=fake.email(),
                password=fake.password(),
                is_superuser=random.choice([True, False]),
            ),
        )

    # Create authors
    author_ids = []
    for _ in range(num_authors):
        author = create_author(db, AuthorCreate(full_name=fake.name()))
        author_ids.append(author.id)

    # Create books
    book_ids = []
    for _ in range(num_books):
        book = create_book(
            db,
            BookCreate(
                title=fake.sentence(),
                description=fake.text(),
                image_url=fake.image_url(),
                author_id=random.choice(author_ids),
                review_hour_amount=random.randint(2, 100),
            ),
        )
        book_ids.append(book.id)

    # Create reviews
    for _ in range(num_reviews):
        user_id = random.randint(1, num_users)
        try:
            create_review(
                db,
                ReviewCreate(
                    book_id=random.choice(book_ids),
                    user_created_id=user_id,
                    text=fake.text(),
                ),
                user_id,
            )
        except Exception as e:
            pass

    # Create likes and dislikes
    for _ in range(num_likes):
        try:
            create_like(
                db,
                random.randint(1, num_users),
                review_id=random.randint(1, num_reviews),
            )
        except Exception as e:
            pass

    for _ in range(num_dislikes):
        try:
            create_dislike(
                db,
                random.randint(1, num_users),
                review_id=random.randint(1, num_reviews),
            )
        except Exception as e:
            pass


def init():
    db = SessionLocal()
    # Clear existing data from all tables
    # Add code to clear data if needed

    create_fake_data(db)


if __name__ == "__main__":
    print("Initializing database with test data...")
    init()
    print("Database initialization complete.")
