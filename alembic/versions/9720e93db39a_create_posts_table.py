"""create posts table

Revision ID: 9720e93db39a
Revises: 
Create Date: 2023-01-17 12:22:29.357149

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9720e93db39a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts", 
                    sa.Column('id', sa.Integer, nullable=False, primary_key=True), 
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')

    pass
