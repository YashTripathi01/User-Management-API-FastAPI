from fastapi import APIRouter, Depends
from marshmallow import ValidationError
from .login_helper import login_user
from ...schemas.auth_schema import LoginPydantic, LoginMarsh

router = APIRouter(tags=['Login'])


@router.post('/login')
def login(request: LoginPydantic):
    try:
        data = dict(request)
        LoginMarsh().load(data)
    except ValidationError as e:
        return e.messages

    return login_user(request=request)
