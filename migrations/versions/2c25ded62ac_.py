"""Add table property

Revision ID: 2c25ded62ac
Revises: 59e181e5e82
Create Date: 2017-12-28 12:46:14.464584

"""

# revision identifiers, used by Alembic.
revision = '2c25ded62ac'
down_revision = '59e181e5e82'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('property',
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.Column('type', sa.String(length=50), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('town_id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['town_id'], ['town.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('user', 'name',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)


def downgrade():
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('user', 'name',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.drop_table('property')
