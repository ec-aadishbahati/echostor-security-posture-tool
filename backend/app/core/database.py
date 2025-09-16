from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

write_engine = create_engine(settings.DATABASE_URL_WRITE, connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL_WRITE else {})
read_engine = create_engine(settings.DATABASE_URL_READ, connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL_READ else {})

WriteSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=write_engine)
ReadSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=read_engine)

Base = declarative_base()

def get_write_db():
    db = WriteSessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_read_db():
    db = ReadSessionLocal()
    try:
        yield db
    finally:
        db.close()
