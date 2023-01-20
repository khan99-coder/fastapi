"""add content column to posts table

Revision ID: 6529ea702a24
Revises: 9720e93db39a
Create Date: 2023-01-17 13:08:21.716110

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6529ea702a24'
down_revision = '9720e93db39a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
