"""Update field in user table

Revision ID: 30284cf4d7d7
Revises: b75f65f80c1e
Create Date: 2024-07-09 15:45:13.980832

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '30284cf4d7d7'
down_revision: Union[str, None] = 'b75f65f80c1e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('user_name', sa.String(length=20), nullable=False),
    sa.Column('Mobile_No', sa.String(length=10), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('Date_of_Birth', sa.String(length=20), nullable=False),
    sa.Column('Gender', sa.String(length=20), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('is_verified', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
