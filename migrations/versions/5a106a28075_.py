"""Add user table

Revision ID: 5a106a28075
Revises: None
Create Date: 2017-12-27 13:31:48.372437

"""

# revision identifiers, used by Alembic.
revision = '5a106a28075'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('user',
    sa.Column('birth_date', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('user')
