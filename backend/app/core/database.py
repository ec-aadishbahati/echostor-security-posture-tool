import logging
import time

import sentry_sdk
from sqlalchemy import create_engine, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

logger = logging.getLogger(__name__)

SLOW_QUERY_THRESHOLD = 100

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False}
    if settings.DATABASE_URL and "sqlite" in settings.DATABASE_URL
    else {},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


@event.listens_for(engine, "before_cursor_execute")
def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    conn.info.setdefault("query_start_time", []).append(time.time())


@event.listens_for(engine, "after_cursor_execute")
def after_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    total_time = time.time() - conn.info["query_start_time"].pop()
    duration_ms = total_time * 1000

    if duration_ms > SLOW_QUERY_THRESHOLD:
        logger.warning(f"Slow query ({duration_ms:.2f}ms): {statement[:200]}")
        if settings.SENTRY_DSN:
            sentry_sdk.capture_message(
                f"Slow database query: {duration_ms:.2f}ms",
                level="warning",
                extras={"query": statement[:500], "duration_ms": duration_ms},
            )


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
