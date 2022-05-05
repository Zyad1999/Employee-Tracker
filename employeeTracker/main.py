from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from config.database import engine
from entities.models import employee
from entities.models import project, department ,dependent

from routers.root import router

employee.Base.metadata.create_all(engine)
project.Base.metadata.create_all(engine)
department.Base.metadata.create_all(engine)
dependent.Base.metadata.create_all(engine)
from config.environment import (
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