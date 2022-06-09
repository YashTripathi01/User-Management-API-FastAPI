from fastapi import APIRouter, Depends
from typing import List
from ...schemas.user_schema import UserResponse
from ...schemas.company_schema import CompanyResponse
from ...helpers.oauth import get_current_user
from .get_company_helper import getting_all_companies, getting_companies_by_id

router = APIRouter(tags=['Company Panel'])


@router.get('/company', response_model=List[CompanyResponse])
def get_all_companies(current_user: UserResponse = Depends(get_current_user)):
    return getting_all_companies(current_user=current_user)


@router.get('/company/{id}', response_model=CompanyResponse)
def get_companies_by_id(id: int, current_user: UserResponse = Depends(get_current_user)):
    return getting_companies_by_id(id=id, current_user=current_user)
