"""Add town table

Revision ID: 59e181e5e82
Revises: 5a106a28075
Create Date: 2017-12-27 14:02:35.785478

"""

# revision identifiers, used by Alembic.
revision = '59e181e5e82'
down_revision = '5a106a28075'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('town',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('town')
