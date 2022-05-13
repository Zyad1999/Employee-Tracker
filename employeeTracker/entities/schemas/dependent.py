from pydantic import BaseModel
from typing import Optional
from .employee import ShowEmployee

class dependent(BaseModel):
    gender : str
    name : str
    relation : str
    employee_ssn:int

class showDependent(BaseModel):
    id: int
    gender : str
    name: str
    relation: str
    employee: ShowEmployee
    class Config():
        orm_mode = True

class updateDependent(BaseModel):
    gender: Optional[str]
    name: Optional[str]
    relation: Optional[int]