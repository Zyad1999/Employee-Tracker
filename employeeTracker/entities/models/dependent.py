from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey , FLOAT
Base = declarative_base()
class dependent(Base):

    __tablename__ = 'dependent'

    id = Column(Integer ,primary_key=True, index=True)
    name = Column(String)
    gender = Column(String)
    relationship = Column(String)
