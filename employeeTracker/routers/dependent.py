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
    "/{id}",
    response_model=showDependent,
    status_code=status.HTTP_200_OK,
    summary="Get a Dependent",
    tags=["Dependent"]
)
async def get_one(id:int, db: Session = Depends(get_db)):
    return await dependent_repo.getDependent(id,db)

@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    summary="Delete a Dependent",
    tags=["Dependent"]
)
async def delete_one(id:int, db: Session = Depends(get_db)):
    return await dependent_repo.deleteDependent(id,db)

@router.put('/{id}',
    response_model=showDependent,
    status_code=status.HTTP_200_OK,
    summary="Update Dependent",
    tags=["Dependent"]
)
async def update_one(id:int, dependent: updateDependent, db: Session = Depends(get_db)):
    return await dependent_repo.updateDependent(id,dependent.dict(), db)