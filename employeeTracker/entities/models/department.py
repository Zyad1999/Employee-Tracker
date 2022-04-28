from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey , FLOAT
Base = declarative_base()
class department(Base):

    __tablename__ = 'department'

    id =  Column(Integer ,primary_key=True, index=True)
    location = Column(String)
    name = Column(String)
    number_employee = Column(Integer)
