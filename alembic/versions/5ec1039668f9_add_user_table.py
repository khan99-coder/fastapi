"""add user table

Revision ID: 5ec1039668f9
Revises: 6529ea702a24
Create Date: 2023-01-17 13:29:00.139320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ec1039668f9'
down_revision = '6529ea702a24'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users", 
                    sa.Column('id', sa.INTEGER, nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'), 
                    sa.UniqueConstraint('email') 
                    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
