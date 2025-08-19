"""create phone number for user column

Revision ID: d2dc2c5e43ab
Revises: 
Create Date: 2025-08-19 15:31:43.346764

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd2dc2c5e43ab'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number', sa.String(10), nullable=True))



def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users','phone_number')
