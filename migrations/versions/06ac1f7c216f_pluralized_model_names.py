"""pluralized model names

Revision ID: 06ac1f7c216f
Revises: abbec0331e1a
Create Date: 2024-05-09 11:40:32.605532

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '06ac1f7c216f'
down_revision: Union[str, None] = 'abbec0331e1a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
