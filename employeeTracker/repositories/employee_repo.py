import email
from unicodedata import name
from sqlalchemy.orm import Session
from ..entities.models.employee import Employee as employee_model
from ..entities.schemas.employee import Employee,ShowEmployee
from fastapi import HTTPException, status
from ..config.hashing import get_password_hash

async def create(newemployee: Employee, db: Session):
    new_employee = employee_model(name=newemployee.name,
                                    email=newemployee.email,
                                    phone=newemployee.phone,
                                    address=newemployee.address,
                                    salary=newemployee.salary,
                                    status=newemployee.status,
                                    birthDate=newemployee.birthDate,
                                    gender=newemployee.gender,
                                    password=get_password_hash(newemployee.password)
                                )
    db.add(new_employee)
    db.commit()
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

    employee.delete(synchronize_session=False)
    db.commit()
    return {"Status":'Deleted'}


async def update_an_employee(ssn: int, newemployee: Employee, db: Session):
    if(newemployee['password']):
        newemployee['password'] = get_password_hash(newemployee['password'])

    employee = db.query(employee_model).filter(employee_model.ssn == ssn)

    if not employee.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Employee with the ssn {ssn} not found")

    employee.update({k: v for k, v in newemployee.items() if v})
    db.commit()
    return employee.first()