from fastapi import APIRouter, Depends
from typing import List
from ...schemas.user_schema import UserResponse
from ...helpers.oauth import get_current_user
from .get_user_helper import getting_all_users, getting_users_by_id

router = APIRouter(tags=['User Panel'])


@router.get('/user', response_model=List[UserResponse])
def get_all_users(current_user: UserResponse = Depends(get_current_user)):
    return getting_all_users(current_user=current_user)


@router.get('/user/{id}', response_model=UserResponse)
def get_users_by_id(id: int, current_user: UserResponse = Depends(get_current_user)):
    return getting_users_by_id(id=id, current_user=current_user)
