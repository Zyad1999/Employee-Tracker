import logging
import sys
import os
from datetime import timedelta
from typing import List
from loguru import logger
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

from .loggingp import InterceptHandler

API_PREFIX = "/api"

JWT_TOKEN_PREFIX = "Token"
VERSION = "0.0.0"
ALGORITHM = "HS256"
config = Config(".env", os.environ)
DEBUG: bool = config("DEBUG", cast=bool, default=True)

JWT_EXPIRATION_DELTA = timedelta(
    minutes=config("ACCESS_TOKEN_EXPIRE_MINUTES", cast=int, default=30)
)
JWT_REFRESH_EXPIRATION_DELTA = timedelta(
    minutes=config("ACCESS_TOKEN_EXPIRE_MINUTES", cast=int, default=10080)
)

SECRET_KEY: Secret = config(
    "SECRET_KEY", cast=Secret, default="This is a secret key for development"
)

PROJECT_NAME: str = config("PROJECT_NAME", default="Employee Tracker")
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="",
)

DATABASE_URL: str = config("DATABASE_URL", cast=str, default="")
RESOURCES_NAMES: List[str] = ["employee", "project", "department", "dependent", "degree"]
FILE_UPLOAD_SIZE : str = config("FILE_UPLOAD_SIZE", cast = str, default="4MB")
PRESIGNED_URL_TIME_INTERVAL: str = config("PRESIGNED_URL_TIME_INTERVAL", cast = str, default="3600")

# logging configuration
LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
LOGGERS = ("uvicorn.asgi", "uvicorn.access")

logging.getLogger().handlers = [InterceptHandler()]
for logger_name in LOGGERS:
    logging_logger = logging.getLogger(logger_name)
    logging_logger.handlers = [InterceptHandler(level=LOGGING_LEVEL)]

logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
