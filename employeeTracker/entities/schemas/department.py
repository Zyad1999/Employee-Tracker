from pydantic import BaseModel
from typing import  Optional

class department(BaseModel):
    location : str
    name : str
    number_employee : int

class showDepartment(BaseModel):
    id: int
    location: str
    name: str
    number_employee: int
    class Config():
        orm_mode = True

class updateDepartment(BaseModel):
    location: Optional[str]
    name: Optional[str]
    number_employee: Optional[int]