"""empty message

Revision ID: d0d2393758d2
Revises: d65be60b4b6c
Create Date: 2024-08-16 06:50:20.445805

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = 'd0d2393758d2'
down_revision: Union[str, None] = 'd65be60b4b6c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_archive', sa.Boolean(), server_default=sa.text('false'), nullable=False))
        batch_op.drop_column('is_info')

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_info', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.drop_column('is_archive')

    # ### end Alembic commands ###
