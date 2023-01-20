"""add foreign-key to posts table

Revision ID: d3e6523c824f
Revises: 5ec1039668f9
Create Date: 2023-01-17 13:52:08.894630

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3e6523c824f'
down_revision = '5ec1039668f9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.INTEGER, nullable=False))
    op.create_foreign_key("post_users_fk", source_table='posts', referent_table="users", 
                          local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
