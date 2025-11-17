from typing import Any

"""Test-only helpers for environments without PostgreSQL JSONB support."""

from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.compiler import compiles


@compiles(JSONB, "sqlite")
def compile_jsonb_to_sqlite(type_: Any, compiler: Any, **kwargs: Any) -> str:
    """Render JSONB columns as TEXT when running against SQLite."""
    return "TEXT"
