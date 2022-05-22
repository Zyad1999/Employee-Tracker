import email
from tokenize import String
from typing import Optional, List
from fastapi import APIRouter, HTTPException, Security, Depends, status
from sqlalchemy.orm import Session
from entities.schemas.employee import (
    Employee,
    EmployeeAuthBody,
    ShowEmployee,
    UpdateEmployee,
    AssignEmployee
)

from routers.errors.generate_http_response_openapi import generate_response_for_openapi
from config.database import get_db
from repositories import employee_repo,services
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(responses=generate_response_for_openapi("Employee"))

@router.get(
    "/",
    response_model=List[ShowEmployee],
    status_code=status.HTTP_200_OK,
    summary="Get all employees",
    tags=["Employee"]
)
async def get(db: Session = Depends(get_db),current_user: int = Depends(services.get_current_user)):
    return await employee_repo.get_all(db)

@router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    summary="Login",
    tags=["Employee"]
)
async def get(auth_body: EmployeeAuthBody,db: Session = Depends(get_db)):
    return await services.login_access_token(auth_body,db)

@router.post(
    "/login/swagger",
    status_code=status.HTTP_200_OK,
    summary="Login",
    include_in_schema=False,
    tags=["Employee"]
)
async def get(request: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    auth_body = EmployeeAuthBody(email=request.username,password=request.password)
    return await services.login_access_token(auth_body,db)

@router.post('/',
    response_model=ShowEmployee,
    status_code=status.HTTP_200_OK,
    summary="Add an employee",
    tags=["Employee"]
)
async def create(employee: Employee, db: Session = Depends(get_db),current_user: int = Depends(services.get_current_user)):
    return await employee_repo.create(employee, db)

@router.get(
    "/{ssn}",
    response_model=ShowEmployee,
    status_code=status.HTTP_200_OK,
    summary="Get an employee",
    tags=["Employee"]
)
async def get_one(ssn:int, db: Session = Depends(get_db),current_user: int = Depends(services.get_current_user)):
    return await employee_repo.get_an_employee(ssn,db)

@router.delete(
    "/{ssn}",
    status_code=status.HTTP_200_OK,
    summary="Delete an employee",
    tags=["Employee"]
)
async def delete_one(ssn:int, db: Session = Depends(get_db),current_user: int = Depends(services.get_current_user)):
    return await employee_repo.delete_an_employee(ssn,db)

@router.put('/{ssn}',
    response_model=ShowEmployee,
    status_code=status.HTTP_200_OK,
    summary="Update an employee",
    tags=["Employee"]
)
async def update_one(ssn:int, employee: UpdateEmployee, db: Session = Depends(get_db),current_user: int = Depends(services.get_current_user)):
    return await employee_repo.update_an_employee(ssn,employee.dict(), db)

@router.post('/assign',
    response_model=ShowEmployee,
    status_code=status.HTTP_200_OK,
    summary="Assign employee to a project",
    tags=["Employee"]
)
async def assign_one(assign: AssignEmployee, db: Session = Depends(get_db),current_user: int = Depends(services.get_current_user)):
    return await employee_repo.assign_an_employee(assign, db)