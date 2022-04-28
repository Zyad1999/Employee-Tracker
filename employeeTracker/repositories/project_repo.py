from sqlalchemy.orm import Session
from entities.models.project import project as project_model
from entities.schemas.project import project,showProject
from fastapi import HTTPException, status

async def createProject(newemproject: project, db: Session):
    new_project = project_model(id=newemproject.id,
                                    budget=newemproject.budget,
                                    name=newemproject.name,
                                    location=newemproject.location
                                )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

async def getAllProject(db: Session):
    projects = db.query(project_model).all()
    return projects

async def getProject(id:int, db: Session):
    project = db.query(project_model).filter(project_model.id == id).first()
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Project with the id {id} is not available")
    return project

async def deleteProject(id: int, db: Session):
    project = db.query(project_model).filter(project_model.id == id)

    if not project.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Project with the id {id} not found")

    project.delete(synchronize_session=False)
    db.commit()
    return {"Status":'Deleted'}


async def updateProject(id: int, newemproject: project, db: Session):


    project = db.query(project_model).filter(project_model.id == id)

    if not project.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Project with the id {id} not found")

    project.update({k: v for k, v in newemproject.items() if v})
    db.commit()
    return project.first()