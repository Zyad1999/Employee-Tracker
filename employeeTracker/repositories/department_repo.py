from sqlalchemy.orm import Session
from entities.models.department import department as department_model
from entities.schemas.department import department,showDepartment
from fastapi import HTTPException, status

async def createDepartment(newdepartment: department, db: Session):
    new_department = department_model(number_employee=newdepartment.number_employee,
                                    name=newdepartment.name,
                                    location=newdepartment.location
                                )
    db.add(new_department)
    db.commit()
    db.refresh(new_department)
    return new_department

async def getAllDepartment(db: Session):
    department = db.query(department_model).all()
    return department

async def getDepartment(id:int, db: Session):
    department = db.query(department_model).filter(department_model.
                                                   id == id).first()
    if not department:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Department with the id {id} is not available")
    return department

async def deleteDepartment(id: int, db: Session):
    department = db.query(department_model).filter(department_model.id == id)

    if not department.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Department with the id {id} not found")

    department.delete(synchronize_session=False)
    db.commit()
    return {"Status":'Deleted'}


async def updateDepartment(id: int, newdepartment: department, db: Session):


    department = db.query(department_model).filter(department_model.id == id)

    if not department.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Department with the id {id} not found")

    department.update({k: v for k, v in newdepartment.items() if v})
    db.commit()
    return department.first()