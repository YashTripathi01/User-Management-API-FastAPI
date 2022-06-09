from fastapi import APIRouter, Depends
from ...schemas.user_schema import UserResponse
from ...helpers.oauth import get_current_user
from .delete_user_helper import deleting_user

router = APIRouter(tags=['User Panel'])


@router.delete('/user/{id}')
def delete_user(id: int, current_user: UserResponse = Depends(get_current_user)):
    return deleting_user(id=id, current_user=current_user)
