from typing import List, Optional
from pydantic import BaseModel,EmailStr
from datetime import date
from ..schemas.department import showDepartment
from ..schemas.project import showProject

class Employee(BaseModel):
    fname:str
    mname: str
    lname: str
    degree :str
    email:EmailStr
    phone:str
    address:str
    salary: int
    status:str
    birthDate: date
    gender: str
    password:str
    department_id:int

class ShowEmployeeBase(BaseModel):
    fname:str
    mname: str
    lname: str
    degree:str
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

class ShowEmployee(ShowEmployeeBase):
    department:Optional[showDepartment]
    projects:Optional[List[showProject]]
    class Config():
        orm_mode = True
    
class UpdateEmployee(BaseModel):
    fname:Optional[str]
    lname: Optional[str]
    mname: Optional[str]
    email:Optional[EmailStr]
    degree:Optional[str]
    phone:Optional[str]
    address:Optional[str]
    salary: Optional[int]
    status:Optional[str]
    birthDate: Optional[date]
    gender: Optional[str]
    password:Optional[str]
    department_id:Optional[int]

class AssignEmployee(BaseModel):
    project_id:int
    employee_id:int
    hours:int