from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from employeeTracker.config.database import engine
from employeeTracker.entities.models import employee


from employeeTracker.routers.root import router

employee.Base.metadata.create_all(engine)

from employeeTracker.config.environment import (
    ALLOWED_HOSTS,
    API_PREFIX,
    DEBUG,
    PROJECT_NAME,
    VERSION,
)

def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(router, prefix=API_PREFIX)

    return application

app = get_application()