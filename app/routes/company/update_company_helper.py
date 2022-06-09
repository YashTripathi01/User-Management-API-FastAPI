from fastapi import HTTPException
from http import HTTPStatus
from ...helpers.database_helper import valid_company_name, role_power, update_company
from ...config.error_logs import *


def updating_company(id: int, request, current_user):
    if valid_company_name(request.company_name):
        raise HTTPException(
            status_code=HTTPStatus.ALREADY_REPORTED, detail=COMPANY_ALREADY_EXISTS)

    role = role_power(current_user.id)

    if role == 'SuperAdmin':
        update_company(id, request)
        return HTTPException(status_code=HTTPStatus.ACCEPTED, detail=UPDATE_COMPANY)
    else:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail=USER_UNAUTHORIZED)
