from tokenize import String
from typing import Optional, List
from fastapi import APIRouter, HTTPException, Security, Depends, status
from sqlalchemy.orm import Session
from entities.schemas.dependent import (
    dependent,
    showDependent,
    updateDependent
)

from routers.errors.generate_http_response_openapi import generate_response_for_openapi
from config.database import get_db
from repositories import dependent_repo

router = APIRouter(responses=generate_response_for_openapi("Dependent"))

@router.get(
    "/",
    response_model=List[showDependent],
    status_code=status.HTTP_200_OK,
    summary="Get all Dependent",
    tags=["Dependent"]
)
async def get(db: Session = Depends(get_db)):
    return await dependent_repo.getAllDependent(db)

@router.post('/',
    response_model=showDependent,
    status_code=status.HTTP_200_OK,
    summary="Add a Dependent",
    tags=["Dependent"]
)

async def create(dependent: dependent, db: Session = Depends(get_db)):
    return await dependent_repo.createDependent(dependent, db)

@router.get(
    "/{employee_ssn}",
    response_model=showDependent,
    status_code=status.HTTP_200_OK,
    summary="Get a Dependent",
    tags=["Dependent"]
)
async def get_one(employee_ssn:int, db: Session = Depends(get_db)):
    return await dependent_repo.getDependent(employee_ssn,db)

@router.delete(
    "/{employee_ssn}",
    status_code=status.HTTP_200_OK,
    summary="Delete a Dependent",
    tags=["Dependent"]
)
async def delete_one(employee_ssn:int, db: Session = Depends(get_db)):
    return await dependent_repo.deleteDependent(employee_ssn,db)

@router.put('/{id}',
    response_model=showDependent,
    status_code=status.HTTP_200_OK,
    summary="Update Dependent",
    tags=["Dependent"]
)
async def update_one(employee_ssn:int, dependent: updateDependent, db: Session = Depends(get_db)):
    return await dependent_repo.updateDependent(employee_ssn,dependent.dict(), db)