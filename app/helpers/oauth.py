from jose import JWTError, jwt
from fastapi import Depends, HTTPException
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from http import HTTPStatus
from .constants import *
from ..schemas.auth_schema import TokenDataPydantic
from ..database.database import get_db
from ..models import models

oauth_scheme = OAuth2PasswordBearer(tokenUrl='login')

# create access token
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({'exp': expire})

    encoded_jwt_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt_token


# verify access token
def verify_access_token(token: str, creds_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get('email')

        if not email or email is None:
            raise creds_exception

        token_data = TokenDataPydantic(email=email)
    except JWTError:
        raise creds_exception

    return token_data


# get current user
def get_current_user(token: str = Depends(oauth_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=HTTPStatus.UNAUTHORIZED, headers={'WWW-Authenticate': 'Bearer'})

    token = verify_access_token(token, credentials_exception)
    user = db.query(models.Users).filter(
        models.Users.email == token.email).first()

    if user is None:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED)
    else:
        return user
