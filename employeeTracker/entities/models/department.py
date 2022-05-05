from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey , FLOAT
Base = declarative_base()
from sqlalchemy.orm import relationship
from .project import Project
class Department(Base):

    __tablename__ = 'Department'

    id =  Column(Integer ,primary_key=True, index=True)
    location = Column(String)
    name = Column(String)
    number_employee = Column(Integer)
    #p_control =  relationship(Project.__tablename__,back_populates = "d_control")
