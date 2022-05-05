from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .department import Department

Base  = declarative_base()

class Employee(Base):
    __tablename__ = 'Employee'
    ssn  = Column(Integer, primary_key=True, index=True)
    fname = Column(String)
    lname = Column(String)
    mname =  Column(String)
    email = Column(String)
    phone = Column(String)
    address = Column(String)
    salary = Column(Float)
    status = Column(String)
    birthDate = Column(Date)
    gender = Column(String)
    password = Column(String)
    degree =  Column(String)
    projects = relationship("Project",secondary='Works')
    department_id = Column(Integer, ForeignKey(Department.id))
    department = relationship(Department, back_populates="employees")

    #dependent = relationship("Dependent", back_populates="employee")
