from fastapi import APIRouter, Depends
from marshmallow import ValidationError
from http import HTTPStatus
from .add_user_helper import adding_user
from ...schemas.user_schema import UserPydantic, UserResponse, UserMarsh
from ...helpers.oauth import get_current_user

router = APIRouter(tags=['User Panel'])


@router.post('/user', status_code=HTTPStatus.ACCEPTED)
def add_user(request: UserPydantic, current_user: UserResponse = Depends(get_current_user)):
    try:
        data = dict(request)
        UserMarsh().load(data=data)
    except ValidationError as e:
        return e.messages

    return adding_user(request=request, current_user=current_user)
