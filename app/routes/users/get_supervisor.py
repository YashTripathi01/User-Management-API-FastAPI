from fastapi import APIRouter, Depends
from typing import List
from .get_supervisor_helper import getting_supervisor
from ...schemas.user_schema import UserResponse
from ...helpers.oauth import get_current_user

router = APIRouter(tags=['Supervisor'])


@router.get('/supervisor', response_model=List[UserResponse])
def get_supervisor(current_user: UserResponse = Depends(get_current_user)):
    return getting_supervisor(current_user=current_user)
