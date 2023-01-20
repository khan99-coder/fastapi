"""add last few columns to posts table

Revision ID: 59f514259134
Revises: d3e6523c824f
Create Date: 2023-01-17 15:45:59.753859

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59f514259134'
down_revision = 'd3e6523c824f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), 
                                     nullable=False, server_default='True'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
                                     nullable=False, server_default=sa.text('now()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
