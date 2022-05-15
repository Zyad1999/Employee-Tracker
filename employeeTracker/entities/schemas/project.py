from pydantic import BaseModel
from typing import  Optional

class project(BaseModel):
    location : str
    name : str
    budget : float
    description:str
    department_id:int

class showProject(BaseModel):
    id: int
    location: str
    name: str
    budget: float
    description: str
    department_id:int

    class Config():
        orm_mode = True

class updateProject(BaseModel):
    location: Optional[str]
    name: Optional[str]
    budget: Optional[float]
    description:Optional[str]
    department_id:Optional[int]