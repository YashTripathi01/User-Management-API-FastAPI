from fastapi import HTTPException
from http import HTTPStatus
from ...helpers.database_helper import role_power, get_all_companies, get_companies_by_id
from ...config.error_logs import *


def getting_all_companies(current_user):
    role = role_power(current_user.id)

    if role == 'SuperAdmin':
        res = get_all_companies()
        if res:
            return res
        else:
            raise HTTPException(
                status_code=HTTPStatus.NO_CONTENT, detail=COMPANY_NOT_FOUND)

    else:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail=USER_UNAUTHORIZED)


def getting_companies_by_id(id: int, current_user):
    role = role_power(current_user.id)

    if role == 'SuperAdmin':
        res = get_companies_by_id(id)
        if res:
            return res
        else:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail=COMPANY_NOT_FOUND)

    else:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail=USER_UNAUTHORIZED)
