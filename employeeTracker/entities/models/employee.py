from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .department import Department
from config.database import Base

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
    projects = relationship("Project",secondary='Works',cascade="all, delete",passive_deletes=True)
    department_id = Column(Integer, ForeignKey(Department.id))
    manage_department_id  = Column(Integer, ForeignKey(Department.id))
    manager =  relationship(Department, back_populates="managed")
    department = relationship(Department, back_populates="employees")
    dependents = relationship("Dependent", back_populates="employee",cascade="all, delete",passive_deletes=True)