from fastapi import HTTPException
from http import HTTPStatus
from ...helpers.database_helper import valid_company_name, role_power, add_new_company
from ...config.error_logs import *


def adding_company(request, current_user):
    if valid_company_name(request.company_name):
        raise HTTPException(status_code=HTTPStatus.ALREADY_REPORTED)

    role = role_power(current_user.id)

    if role == 'SuperAdmin':
        add_new_company(request)
        return {'message': ADD_COMPANY}

    else:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED)
