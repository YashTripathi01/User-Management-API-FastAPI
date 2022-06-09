from fastapi import HTTPException
from http import HTTPStatus

from app.config.error_logs import COMPANY_NOT_FOUND, DELETE_COMPANY, USER_UNAUTHORIZED
from ...helpers.database_helper import list_company_id, role_power, delete_company


def deleting_company(id: int, current_user):
    if id == 0:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail=USER_UNAUTHORIZED)

    company_id = list_company_id()

    if id not in company_id:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail=COMPANY_NOT_FOUND)

    role = role_power(current_user.id)

    if role == 'SuperAdmin':
        delete_company(id)
        return {'message': HTTPException(status_code=HTTPStatus.ACCEPTED, detail=DELETE_COMPANY)}

    else:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail=USER_UNAUTHORIZED)
