from pydantic import BaseModel
from typing import  Optional

class project(BaseModel):
    location : str
    name : str
    budget : float
    description:str

class showProject(BaseModel):
    id: int
    location: str
    name: str
    budget: float
    description: str
    class Config():
        orm_mode = True

class updateProject(BaseModel):
    location: Optional[str]
    name: Optional[str]
    budget: Optional[float]
    description:Optional[str]