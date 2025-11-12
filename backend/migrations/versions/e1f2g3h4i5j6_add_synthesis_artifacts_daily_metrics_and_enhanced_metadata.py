"""add_synthesis_artifacts_daily_metrics_and_enhanced_metadata

Revision ID: e1f2g3h4i5j6
Revises: d5f251975256
Create Date: 2025-11-12 05:59:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = 'e1f2g3h4i5j6'
down_revision: Union[str, None] = 'd5f251975256'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'ai_synthesis_artifacts',
        sa.Column('id', sa.String(length=36), nullable=False),
        sa.Column('report_id', sa.String(length=36), nullable=False),
        sa.Column('artifact_json', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column('storage_uri', sa.Text(), nullable=True),
        sa.Column('prompt_version', sa.String(length=20), nullable=False),
        sa.Column('schema_version', sa.String(length=20), nullable=False),
        sa.Column('model', sa.String(length=50), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.ForeignKeyConstraint(['report_id'], ['reports.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index('idx_synthesis_report', 'ai_synthesis_artifacts', ['report_id'], unique=True)

    op.create_table(
        'ai_daily_metrics',
        sa.Column('id', sa.String(length=36), nullable=False),
        sa.Column('date', sa.Date(), nullable=False),
        sa.Column('total_reports', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('total_sections', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('total_tokens_prompt', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('total_tokens_completion', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('total_cost_usd', sa.DECIMAL(precision=10, scale=2), nullable=False, server_default='0'),
        sa.Column('avg_latency_ms', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('cache_hit_rate', sa.DECIMAL(precision=5, scale=2), nullable=False, server_default='0'),
        sa.Column('success_rate', sa.DECIMAL(precision=5, scale=2), nullable=False, server_default='0'),
        sa.Column('degraded_rate', sa.DECIMAL(precision=5, scale=2), nullable=False, server_default='0'),
        sa.Column('created_at', sa.Date(), server_default=sa.text('CURRENT_DATE'), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index('idx_daily_metrics_date', 'ai_daily_metrics', ['date'], unique=True)

    op.add_column('ai_generation_metadata', sa.Column('attempt_count', sa.Integer(), nullable=False, server_default='1'))
    op.add_column('ai_generation_metadata', sa.Column('error_code', sa.String(length=50), nullable=True))
    op.add_column('ai_generation_metadata', sa.Column('error_message', sa.String(), nullable=True))
    op.add_column('ai_generation_metadata', sa.Column('fallback_model', sa.String(length=50), nullable=True))
    op.add_column('ai_generation_metadata', sa.Column('is_degraded', sa.Integer(), nullable=False, server_default='0'))
    op.add_column('ai_generation_metadata', sa.Column('last_retry_at', sa.DateTime(timezone=True), nullable=True))


def downgrade() -> None:
    op.drop_column('ai_generation_metadata', 'last_retry_at')
    op.drop_column('ai_generation_metadata', 'is_degraded')
    op.drop_column('ai_generation_metadata', 'fallback_model')
    op.drop_column('ai_generation_metadata', 'error_message')
    op.drop_column('ai_generation_metadata', 'error_code')
    op.drop_column('ai_generation_metadata', 'attempt_count')

    op.drop_index('idx_daily_metrics_date', table_name='ai_daily_metrics')
    op.drop_table('ai_daily_metrics')

    op.drop_index('idx_synthesis_report', table_name='ai_synthesis_artifacts')
    op.drop_table('ai_synthesis_artifacts')
