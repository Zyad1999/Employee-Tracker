from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base  = declarative_base()

class Employee(Base):
    __tablename__ = 'Employee'
    ssn  = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    address = Column(String)
    salary = Column(Float)
    status = Column(String)
    birthDate = Column(Date)
    gender = Column(String)
    password = Column(String)