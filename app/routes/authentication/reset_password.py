from fastapi import APIRouter
from http import HTTPStatus
from marshmallow import ValidationError
from .reset_password_helper import reset_user_password
from ...schemas.auth_schema import ResetPassPydantic, ResetPassMarsh

router = APIRouter(tags=['Reset Password'])


@router.post('/reset_password', status_code=HTTPStatus.ACCEPTED)
async def reset_password(request: ResetPassPydantic):
    try:
        data = dict(request)
        ResetPassMarsh().load(data)
    except ValidationError as e:
        return e.messages

    return await reset_user_password(request=request)
