from enum import Enum

from fastapi import status
from fastapi.routing import APIRouter
from pydantic import BaseModel, Field

from config.environment import PROJECT_NAME, API_PREFIX

from routers.employee import router as employeeRouter
from routers.project import router as projectRouter
from routers.department import router as departmentRouter
router = APIRouter()

router.include_router(employeeRouter, prefix="/employee")
router.include_router(projectRouter,prefix="/project")
router.include_router(departmentRouter,prefix="/department")
class StatusEnum(str, Enum):
    OK = "OK"
    FAILURE = "FAILURE"
    CRITICAL = "CRITICAL"
    UNKNOWN = "UNKNOWN"

class HealthCheck(BaseModel):
    title: str = Field(..., description="API title")
    description: str = Field(..., description="Brief description of the API")
    version: str = Field(..., description="API server version number")
    status: StatusEnum = Field(..., description="API current status")

@router.get(
    "/status",
    response_model=HealthCheck,
    status_code=status.HTTP_200_OK,
    tags=["Health Check"],
    summary="Performs health check",
    description="Performs health check and returns information about running service.",
)
def health_check():
    return {
        "title": PROJECT_NAME,
        "description": "This is a test desc",
        "version": API_PREFIX,
        "status": StatusEnum.OK,
    }