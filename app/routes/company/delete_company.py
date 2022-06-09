from fastapi import APIRouter, Depends
from ...schemas.user_schema import UserResponse
from ...helpers.oauth import get_current_user
from .delete_company_helper import deleting_company

router = APIRouter(tags=['Company Panel'])


@router.delete('/company/{id}')
def delete_company(id: int, current_user: UserResponse = Depends(get_current_user)):
    return deleting_company(id=id, current_user=current_user)
