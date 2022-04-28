from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey , FLOAT
Base = declarative_base()
class project(Base):

    __tablename__ = 'project'

    id =  Column(Integer ,primary_key=True, index=True)
    location = Column(String)
    name = Column(String)
    budget = Column(FLOAT)
