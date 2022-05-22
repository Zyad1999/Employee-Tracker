import email
import imp
from unicodedata import name
from sqlalchemy.orm import Session
from entities.models.employee import Employee as employee_model
from entities.models.project import Project,Works
from entities.schemas.employee import Employee,ShowEmployee,AssignEmployee
from fastapi import HTTPException, status
from config.hashing import get_password_hash
from datetime import date
from .department_repo import updateDepartment

async def create(newemployee: Employee, db: Session):
    new_employee = employee_model(  fname=newemployee.fname,
                                    lname=newemployee.lname,
                                    mname=newemployee.mname,
                                    email=newemployee.email,
                                    phone=newemployee.phone,
                                    address=newemployee.address,
                                    salary=newemployee.salary,
                                    status=newemployee.status,
                                    birthDate=newemployee.birthDate,
                                    gender=newemployee.gender,
                                    degree =  newemployee.degree,
                                    password=get_password_hash(newemployee.password),
                                    department_id=newemployee.department_id                                )
    db.add(new_employee)
    db.commit()
    await updateDepartment(newemployee.department_id,{"number_employee":db.query(employee_model).filter(employee_model.department_id == newemployee.department_id).count()},db)
    db.refresh(new_employee)
    return new_employee

async def get_all(db: Session):
    employees = db.query(employee_model).all()
    return employees

async def get_an_employee(ssn:int, db: Session):
    employee = db.query(employee_model).filter(employee_model.ssn == ssn).first()
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Employee with the ssn {ssn} is not available")
    return employee

async def delete_an_employee(ssn: int, db: Session):
    employee = db.query(employee_model).filter(employee_model.ssn == ssn)

    if not employee.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Employee with the ssn {ssn} not found")
    demployee = employee.first()
    emp_department = demployee.department_id

    employee.delete(synchronize_session=False)
    db.commit()
    await updateDepartment(emp_department,{"number_employee":db.query(employee_model).filter(employee_model.department_id == emp_department).count()},db)
    return {"Status":'Deleted'}


async def update_an_employee(ssn: int, newemployee: Employee, db: Session):
    if(newemployee['password']):
        newemployee['password'] = get_password_hash(newemployee['password'])

    employee = db.query(employee_model).filter(employee_model.ssn == ssn)

    if not employee.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Employee with the ssn {ssn} not found")
    old_employee = employee.first()
    old_department = old_employee.department_id

    employee.update({k: v for k, v in newemployee.items() if v})
    db.commit()
    if(newemployee["department_id"]):
        await updateDepartment(old_department,{"number_employee":db.query(employee_model).filter(employee_model.department_id == old_department).count()},db)
        await updateDepartment(newemployee['department_id'],{"number_employee":db.query(employee_model).filter(employee_model.department_id == newemployee['department_id']).count()},db)
    
    return employee.first()

async def assign_an_employee(assign:AssignEmployee, db: Session):

    employee = db.query(employee_model).filter(employee_model.ssn == assign.employee_id)
    project = db.query(Project).filter(Project.id == assign.project_id)
    if not employee.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Employee with the ssn {assign.employee_id} not found")
    if not project.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Project with the id {assign.project_id} not found")

    new_assign = Works(employee_id=assign.employee_id,
                        project_id=assign.project_id,
                        hours=assign.hours,
                        start_date=date.today())
    db.add(new_assign)
    db.commit()
    db.refresh(new_assign)
    return await get_an_employee(assign.employee_id,db)
