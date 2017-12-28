"""Add table room

Revision ID: 2eaef6f5c8c
Revises: 2c25ded62ac
Create Date: 2017-12-28 12:54:02.810103

"""

# revision identifiers, used by Alembic.
revision = '2eaef6f5c8c'
down_revision = '2c25ded62ac'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('room',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('characteristic', sa.String(length=200), nullable=False),
    sa.Column('property_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['property_id'], ['property.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('room')
