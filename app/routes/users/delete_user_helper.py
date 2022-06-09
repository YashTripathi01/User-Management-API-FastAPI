from fastapi import HTTPException
from http import HTTPStatus
from ...helpers.database_helper import get_user_id, role_power, delete_super_admin, delete_admin, delete_supervisor
from ...config.error_logs import *


def deleting_user(id: int, current_user):
    role = role_power(current_user.id)

    if role == 'User':
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail=USER_UNAUTHORIZED)

    if id == 1:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail=USER_UNAUTHORIZED)

    to_delete = get_user_id(id)

    if not to_delete:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail=USER_NOT_FOUND)

    if role == 'SuperAdmin':
        return delete_super_admin(id)

    elif role == 'Admin':
        if current_user.co_id == to_delete.co_id:
            return delete_admin(id)
        else:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED, detail=USER_UNAUTHORIZED)

    elif role == 'Supervisor':
        if current_user.co_id == to_delete.co_id:
            return delete_supervisor(id)
        else:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED, detail=USER_UNAUTHORIZED)

    else:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail=USER_UNAUTHORIZED)
