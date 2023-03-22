"""create notes table

Revision ID: df17d09754cc
Revises: 
Create Date: 2023-03-18 19:55:18.083084

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'df17d09754cc'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
  op.create_table(
    'notes',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('title', sa.String, nullable=False),
    sa.Column('completed', sa.Boolean, nullable=True, default=False),
    sa.Column('order', sa.Integer, nullable=True),
  )

def downgrade() -> None:
  op.drop_table('notes')
