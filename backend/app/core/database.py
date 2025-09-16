from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

write_engine = create_engine(settings.DATABASE_URL_WRITE)
read_engine = create_engine(settings.DATABASE_URL_READ)

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
