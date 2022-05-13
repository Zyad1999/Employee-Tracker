from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey , FLOAT,Date
from sqlalchemy.orm import relationship
from .employee import Employee
#from .department import Department
from config.database import Base
class Project(Base):

    __tablename__ = 'Project'

    id =  Column(Integer ,primary_key=True, index=True)
    location = Column(String)
    description = Column(String)
    name =  Column(String)
    budget = Column(FLOAT)
    employees = relationship('Employee', secondary = 'Works')

class Works(Base):
    __tablename__ = 'Works'
    project_id = Column(Integer, ForeignKey('Project.id'), primary_key = True)
    employee_id = Column(Integer, ForeignKey(Employee.ssn, ondelete="CASCADE"), primary_key = True)
    hours =  Column(Integer)
    start_date = Column(Date)


