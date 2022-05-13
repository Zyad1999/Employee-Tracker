from tokenize import String
from typing import Optional, List
from fastapi import APIRouter, HTTPException, Security, Depends, status
from sqlalchemy.orm import Session
from entities.schemas.employee import (
    Employee,
    ShowEmployee,
    UpdateEmployee,
    AssignEmployee
)

from routers.errors.generate_http_response_openapi import generate_response_for_openapi
from config.database import get_db
from repositories import employee_repo

router = APIRouter(responses=generate_response_for_openapi("Employee"))

@router.get(
    "/",
    response_model=List[ShowEmployee],
    status_code=status.HTTP_200_OK,
    summary="Get all employees",
    tags=["Employee"]
)
async def get(db: Session = Depends(get_db)):
    return await employee_repo.get_all(db)

@router.post('/',
    response_model=ShowEmployee,
    status_code=status.HTTP_200_OK,
    summary="Add an employee",
    tags=["Employee"]
)
async def create(employee: Employee, db: Session = Depends(get_db)):
    return await employee_repo.create(employee, db)

@router.get(
    "/{ssn}",
    response_model=ShowEmployee,
    status_code=status.HTTP_200_OK,
    summary="Get an employee",
    tags=["Employee"]
)
async def get_one(ssn:int, db: Session = Depends(get_db)):
    return await employee_repo.get_an_employee(ssn,db)

@router.delete(
    "/{ssn}",
    status_code=status.HTTP_200_OK,
    summary="Delete an employee",
    tags=["Employee"]
)
async def delete_one(ssn:int, db: Session = Depends(get_db)):
    return await employee_repo.delete_an_employee(ssn,db)

@router.put('/{ssn}',
    response_model=ShowEmployee,
    status_code=status.HTTP_200_OK,
    summary="Update an employee",
    tags=["Employee"]
)
async def update_one(ssn:int, employee: UpdateEmployee, db: Session = Depends(get_db)):
    return await employee_repo.update_an_employee(ssn,employee.dict(), db)

@router.post('/assign',
    response_model=ShowEmployee,
    status_code=status.HTTP_200_OK,
    summary="Assign employee to a project",
    tags=["Employee"]
)
async def assign_one(assign: AssignEmployee, db: Session = Depends(get_db)):
    return await employee_repo.assign_an_employee(assign, db)