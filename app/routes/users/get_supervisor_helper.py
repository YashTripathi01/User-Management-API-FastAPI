from fastapi import HTTPException
from http import HTTPStatus
from ...helpers.database_helper import role_power, get_supervisor_super_admin, get_supervisor_admin_supervisor
from ...config.error_logs import *


def getting_supervisor(current_user):
    role = role_power(current_user.id)

    if role == 'SuperAdmin':
        res = get_supervisor_super_admin()
        if res:
            return res
        else:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail=USER_NOT_FOUND)

    elif role in ['Admin', 'Supervisor']:
        res = get_supervisor_admin_supervisor(current_user.co_id)
        if res:
            return res
        else:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail=USER_NOT_FOUND)

    else:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail=USER_UNAUTHORIZED)
