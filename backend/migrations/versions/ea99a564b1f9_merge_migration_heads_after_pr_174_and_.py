"""merge migration heads after PR 174 and 175

Revision ID: ea99a564b1f9
Revises: 9a260f32567c, e1f2g3h4i5j6
Create Date: 2025-11-12 06:16:53.445187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea99a564b1f9'
down_revision = ('9a260f32567c', 'e1f2g3h4i5j6')
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
