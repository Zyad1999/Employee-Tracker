from typing import List, Optional
from pydantic import BaseModel,EmailStr
from datetime import date

class Employee(BaseModel):
    name:str
    email:EmailStr
    phone:str
    address:str
    salary: int
    status:str
    birthDate: date
    gender: str
    password:str

class ShowEmployee(BaseModel):
    name:str
    email:EmailStr
    phone:str
    address:str
    salary: int
    status:str
    birthDate: date
    gender: str
    ssn: str
    class Config():
        orm_mode = True

class UpdateEmployee(BaseModel):
    name:Optional[str]
    email:Optional[EmailStr]
    phone:Optional[str]
    address:Optional[str]
    salary: Optional[int]
    status:Optional[str]
    birthDate: Optional[date]
    gender: Optional[str]
    password:Optional[str]