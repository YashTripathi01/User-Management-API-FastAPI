from fastapi import APIRouter, Depends
from marshmallow import ValidationError
from .update_company_helper import updating_company
from ...schemas.company_schema import CompanyPydantic, CompanyMarsh, CompanyResponse
from ...schemas.user_schema import UserResponse
from ...helpers.oauth import get_current_user


router = APIRouter(tags=['Company Panel'])


@router.put('/company/{id}')
def update_company(id: int, request: CompanyPydantic, current_user: UserResponse = Depends(get_current_user)):
    try:
        data = dict(request)
        CompanyMarsh().load(data)
    except ValidationError as e:
        return e.messages

    return updating_company(id=id, request=request, current_user=current_user)
