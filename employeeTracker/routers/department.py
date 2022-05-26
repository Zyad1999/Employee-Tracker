from tokenize import String
from typing import Optional, List
from fastapi import APIRouter, HTTPException, Security, Depends, status
from sqlalchemy.orm import Session
from entities.schemas.department import (
    department,
    showDepartment,
    updateDepartment
)

from routers.errors.generate_http_response_openapi import generate_response_for_openapi
from config.database import get_db
from repositories import department_repo,services

router = APIRouter(responses=generate_response_for_openapi("Department"))

@router.get(
    "/",
    response_model=List[showDepartment],
    status_code=status.HTTP_200_OK,
    summary="Get all Departments",
    tags=["Departments"]
)
async def get(db: Session = Depends(get_db),current_user: int = Depends(services.get_current_user)):
    return await department_repo.getAllDepartment(db)

@router.post('/',
    response_model=showDepartment,
    status_code=status.HTTP_200_OK,
    summary="Add a Department",
    tags=["Departments"]
)

async def create(department: department, db: Session = Depends(get_db)):
    return await department_repo.createDepartment(department, db)

@router.get(
    "/{id}",
    response_model=showDepartment,
    status_code=status.HTTP_200_OK,
    summary="Get a Department",
    tags=["Departments"]
)
async def get_one(id:int, db: Session = Depends(get_db),current_user: int = Depends(services.get_current_user)):
    return await department_repo.getDepartment(id,db)

@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    summary="Delete a Department",
    tags=["Departments"]
)
async def delete_one(id:int, db: Session = Depends(get_db),current_user: int = Depends(services.get_current_user)):
    return await department_repo.deleteDepartment(id,db)

@router.put('/{id}',
    response_model=showDepartment,
    status_code=status.HTTP_200_OK,
    summary="Update Department",
    tags=["Departments"]
)
async def update_one(id:int, department: updateDepartment, db: Session = Depends(get_db),current_user: int = Depends(services.get_current_user)):
    return await department_repo.updateDepartment(id,department.dict(), db)