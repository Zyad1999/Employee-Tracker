from tokenize import String
from typing import Optional, List
from fastapi import APIRouter, HTTPException, Security, Depends, status
from sqlalchemy.orm import Session
from entities.schemas.project import (
    project,
    showProject,
    updateProject
)

from routers.errors.generate_http_response_openapi import generate_response_for_openapi
from config.database import get_db
from repositories import project_repo,services

router = APIRouter(responses=generate_response_for_openapi("Project"))

@router.get(
    "/",
    response_model=List[showProject],
    status_code=status.HTTP_200_OK,
    summary="Get all Projects",
    tags=["Projects"]
)
async def get(db: Session = Depends(get_db),current_user: int = Depends(services.get_current_user)):
    return await project_repo.getAllProject(db)

@router.post('/',
    response_model=showProject,
    status_code=status.HTTP_200_OK,
    summary="Add a Project",
    tags=["Projects"]
)

async def create(project: project, db: Session = Depends(get_db),current_user: int = Depends(services.get_current_user)):
    return await project_repo.createProject(project, db)

@router.get(
    "/{id}",
    response_model=showProject,
    status_code=status.HTTP_200_OK,
    summary="Get a Project",
    tags=["Projects"]
)
async def get_one(id:int, db: Session = Depends(get_db),current_user: int = Depends(services.get_current_user)):
    return await project_repo.getProject(id,db)

@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    summary="Delete a Project",
    tags=["Projects"]
)
async def delete_one(id:int, db: Session = Depends(get_db),current_user: int = Depends(services.get_current_user)):
    return await project_repo.deleteProject(id,db)

@router.put('/{id}',
    response_model=showProject,
    status_code=status.HTTP_200_OK,
    summary="Update Project",
    tags=["Projects"]
)
async def update_one(id:int, project: updateProject, db: Session = Depends(get_db),current_user: int = Depends(services.get_current_user)):
    return await project_repo.updateProject(id,project.dict(), db)