from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey , FLOAT
from typing import List
from sqlalchemy.orm import relationship
from config.database import Base
from .employee import Employee

class Dependent(Base):

    __tablename__ = 'Dependent'

    id = Column(Integer, primary_key=True,index = True)
    name = Column(String)
    gender = Column(String)
    relation = Column(String)
    employee_ssn = Column(Integer, ForeignKey(Employee.ssn, ondelete="CASCADE"))
    employee = relationship(Employee, back_populates="dependents")