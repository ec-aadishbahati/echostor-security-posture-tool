"""add selected_section_ids to assessments

Revision ID: 1762153457
Revises: d1e2f3a4b5c6
Create Date: 2025-11-03 07:05:00.000000

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "1762153457"
down_revision = "d1e2f3a4b5c6"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "assessments",
        sa.Column("selected_section_ids", postgresql.JSON(astext_type=sa.Text()), nullable=True),
    )


def downgrade() -> None:
    op.drop_column("assessments", "selected_section_ids")
