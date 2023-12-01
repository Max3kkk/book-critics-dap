"""empty message

Revision ID: 67f4449e56ab
Revises: 91979b40eb38
Create Date: 2023-12-01 08:57:47.593312-08:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67f4449e56ab'
down_revision = '91979b40eb38'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('user', 'is_active')
    op.drop_column('user', 'address')
    op.create_table(
        'author',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('full_name', sa.String(100), nullable=False),
    )
    op.create_table(
        'book',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(100), nullable=False),
        sa.Column('description', sa.String(100), nullable=False),
        sa.Column('image_url', sa.String(100), nullable=False),
        sa.Column('author_id', sa.Integer, sa.ForeignKey('author.id')),
    )
    op.create_table(
        'review',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('text', sa.String(100), nullable=False),
        sa.Column('user_created_id', sa.Integer, sa.ForeignKey('user.id')),
        sa.Column('book_id', sa.Integer, sa.ForeignKey('book.id')),
    )
    op.create_table(
        'like',
        sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id')),
        sa.Column('review_id', sa.Integer, sa.ForeignKey('review.id')),
        sa.PrimaryKeyConstraint('user_id', 'review_id'),
    )
    op.create_table(
        'dislike',
        sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id')),
        sa.Column('review_id', sa.Integer, sa.ForeignKey('review.id')),
        sa.PrimaryKeyConstraint('user_id', 'review_id'),
    )


def downgrade():
    op.drop_table('like')
    op.drop_table('review')
    op.drop_table('book')
    op.drop_table('author')
    op.drop_table('user')
