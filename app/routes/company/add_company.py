from fastapi import APIRouter, Depends
from marshmallow import ValidationError
from .add_company_helper import adding_company
from ...helpers.oauth import get_current_user
from ...schemas.company_schema import CompanyPydantic, CompanyMarsh, CompanyResponse
from ...schemas.user_schema import UserResponse

router = APIRouter(tags=['Company Panel'])


@router.post('/company')
def add_company(request: CompanyPydantic, current_user: UserResponse = Depends(get_current_user)):
    try:
        data = dict(request)
        CompanyMarsh().load(data)
    except ValidationError as e:
        return e.messages

    return adding_company(request=request, current_user=current_user)
