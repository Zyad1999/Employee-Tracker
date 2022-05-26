from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.environment import DATABASE_URL
from sqlalchemy import MetaData

SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://postgres:admin@localhost/employetracker2'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)
meta = MetaData(engine)
meta.reflect()
meta.drop_all()
    
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
