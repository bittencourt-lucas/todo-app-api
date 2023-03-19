"""update notes table to add new properties

Revision ID: 54f1fe77b698
Revises: df17d09754cc
Create Date: 2023-03-19 20:02:54.025547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54f1fe77b698'
down_revision = 'df17d09754cc'
branch_labels = None
depends_on = None


def upgrade() -> None:
  op.add_column('notes', sa.Column('completed', sa.Boolean, nullable=True, default=False))
  op.add_column('notes', sa.Column('url', sa.String, nullable=True))
  op.add_column('notes', sa.Column('order', sa.Integer, nullable=True))
  op.drop_column('notes', 'content')

def downgrade() -> None:
  op.add_column('notes', sa.Column('content', sa.String, nullable=True))
  op.drop_column('notes', 'order')
  op.drop_column('notes', 'url')
  op.drop_column('notes', 'completed')
