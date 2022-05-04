from pydantic import BaseModel
from typing import Optional


class dependent(BaseModel):
    id: int
    gender : str
    name : str
    relationship : str

class showDependent(BaseModel):
    id: int
    gender : str
    name: str
    relationship: str
    class Config():
        orm_mode = True

class updateDependent(BaseModel):
    gender: Optional[str]
    name: Optional[str]
    relationship: Optional[int]