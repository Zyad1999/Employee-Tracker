from datetime import datetime, timedelta
from re import U
from fastapi import Depends, HTTPException, status, Query
from typing import Optional
from jose import jwt
from pydantic import ValidationError
import uuid
from . import employee_repo
from entities.schemas.employee import EmployeeAuthBody,Token,TokenPayload
from config.hashing import verify_password
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
SECRET_KEY = "THIS IS DEVELOPMENT SECRET KEY"
JWT_EXPIRATION_DELTA = timedelta(minutes=20)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None,SCRET_KEY_SALT: Optional[str]=""):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, (str(SECRET_KEY)+SCRET_KEY_SALT), algorithm=str("HS256"))
    return encoded_jwt


async def login_access_token( user: EmployeeAuthBody,db) -> Token:
    user_to_auth = await employee_repo.get_an_employee_by_email(user.email,db)

    user_hash = user_to_auth.password

    if not verify_password(user.password, user_hash):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Wrong Email or Password")
    token_payload = TokenPayload(ssn=user_to_auth.ssn)
    return Token(
        access_token=create_access_token(
            token_payload.dict(), expires_delta=JWT_EXPIRATION_DELTA
        ),
        token_type="bearer"
    )
reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl="/api/employee/login/swagger"
)
async def get_current_user(
    token: str = Depends(reusable_oauth2)):
    try:
        payload = jwt.decode(token, str(SECRET_KEY), algorithms=["HS256"])
        if payload.get("ssn") is None:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Can not validate Credintials")
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    except Exception as e:
        raise e

    return token_data.ssn