"""Remove one column

Revision ID: d926742b61b4
Revises: 59839ad37ac0
Create Date: 2025-05-12 22:07:07.625747

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd926742b61b4'
down_revision: Union[str, None] = '59839ad37ac0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_blocked')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_blocked', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
