from pydantic import BaseModel
from typing import  Optional

class project(BaseModel):
    id: int
    location : str
    name : str
    budget : float

class showProject(BaseModel):
    id: int
    location: str
    name: str
    budget: float
    class Config():
        orm_mode = True

class updateProject(BaseModel):
    location: Optional[str]
    name: Optional[str]
    budget: Optional[float]