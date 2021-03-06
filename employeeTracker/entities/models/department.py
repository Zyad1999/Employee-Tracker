from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey , FLOAT
from config.database import Base
from sqlalchemy.orm import relationship
class Department(Base):

    __tablename__ = 'Department'

    id =  Column(Integer ,primary_key=True, index=True)
    location = Column(String)
    name = Column(String)
    number_employee = Column(Integer)

    employees = relationship("Employee", back_populates="department")
    p_control =  relationship('Project',back_populates = 'd_control')
