from sqlalchemy.orm import Session
from entities.models.dependent import Dependent as dependent_model
from entities.schemas.dependent import dependent,showDependent
from fastapi import HTTPException, status

async def createDependent(new_dependent: dependent, db: Session):
    new_dependent= dependent_model(gender=new_dependent.gender,
                                    name=new_dependent.name,
                                    relation=new_dependent.relation,
                                    employee_ssn=new_dependent.employee_ssn,
                                )
    db.add(new_dependent)
    db.commit()
    db.refresh(new_dependent)
    return new_dependent

async def getAllDependent(db: Session):
    dependent = db.query(dependent_model).all()
    return dependent

async def getDependent(employee_ssn:int, db: Session):
    dependent= db.query(dependent_model).filter(dependent_model.employee_ssn == employee_ssn).first()
    if not dependent:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Dependent with the id {employee_ssn} is not available")
    return dependent

async def deleteDependent(employee_ssn: int, db: Session):
    dependent = db.query(dependent_model).filter(dependent_model.employee_ssn == employee_ssn)

    if not dependent.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Dependent with the id {employee_ssn} not found")

    dependent.delete(synchronize_session=False)
    db.commit()
    return {"Status":'Deleted'}


async def updateDependent(employee_ssn: int, newdependent: dependent, db: Session):


    dependent = db.query(dependent_model).filter(dependent_model.employee_ssn == employee_ssn)

    if not dependent.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Dependent with the id {employee_ssn} not found")

    dependent.update({k: v for k, v in newdependent.items() if v})
    db.commit()
    return dependent.first()