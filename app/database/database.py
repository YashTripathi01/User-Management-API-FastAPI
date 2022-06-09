from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from .constants import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base = declarative_base()

session = Session(bind=engine, expire_on_commit=False)


def get_db():
    db = session
    try:
        yield db
    except:
        db.close()
