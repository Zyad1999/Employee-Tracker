from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey , FLOAT
from sqlalchemy.orm import relationship
from .employee import Employee
#from .department import Department
Base = declarative_base()
class Project(Base):

    __tablename__ = 'Project'

    id =  Column(Integer ,primary_key=True, index=True)
    location = Column(String)
    description = Column(String)
    name =  Column(String)
    budget = Column(FLOAT)
    employees = relationship('Employee', secondary = 'Works')
    #d_control =  relationship(Department.__tablename__,back_populates = "p_control")

class Link(Base):
    __tablename__ = 'Works'
    project_id = Column(Integer, ForeignKey('Project.id'), primary_key = True)
    employee_id = Column(Integer, ForeignKey(Employee.ssn), primary_key = True)


