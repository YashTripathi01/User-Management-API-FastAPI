from fastapi import APIRouter, Depends
from marshmallow import ValidationError
from .update_user_helper import updating_user
from ...schemas.user_schema import UserUpdatePydantic, UserUpdateMarsh, UserResponse
from ...helpers.oauth import get_current_user

router = APIRouter(tags=['User Panel'])


@router.put('/user/{id}')
def update_user(id: int, request: UserUpdatePydantic, current_user: UserResponse = Depends(get_current_user)):
    try:
        data = dict(request)
        UserUpdateMarsh().load(data)
    except ValidationError as e:
        return e.messages

    return updating_user(id=id, request=request, current_user=current_user)
