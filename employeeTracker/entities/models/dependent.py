from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey , FLOAT
from typing import List
from sqlalchemy.orm import relationship
from config.database import Base
from .employee import Employee
from sqlalchemy.schema import PrimaryKeyConstraint

class Dependent(Base):

    __tablename__ = 'Dependent'

    name = Column(String,primary_key=True)
    gender = Column(String)
    relation = Column(String)
    employee_ssn = Column(Integer, ForeignKey(Employee.ssn, ondelete="CASCADE"),primary_key=True )
    employee = relationship(Employee, back_populates="dependents")
    __table_args__ = (
        PrimaryKeyConstraint(name, employee_ssn),
    )