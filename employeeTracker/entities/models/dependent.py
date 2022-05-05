from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey , FLOAT
from typing import List
from sqlalchemy.orm import relationship
Base = declarative_base()

class Dependent(Base):

    __tablename__ = 'dependent'

    #emp_id = Column(Integer ,ForeignKey('Employee.id'))
    id = Column(Integer, primary_key=True,index = True)
    name = Column(String)
    gender = Column(String)
    relationship = Column(String)

    #employee =  relationship("Employee",back_populates = "dependent")
