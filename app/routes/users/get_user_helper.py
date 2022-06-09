from fastapi import HTTPException
from http import HTTPStatus
from ...config.error_logs import *
from ...helpers.database_helper import role_power, get_all_user, get_admin, get_supervisor, get_user_id, get_admin_id, get_supervisor_id


def getting_all_users(current_user):
    role = role_power(current_user.id)

    if role == 'SuperAdmin':
        users = get_all_user()
        if users:
            return users
        else:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail=USER_NOT_FOUND)

    elif role == 'Admin':
        users = get_admin(current_user)
        if users:
            return users
        else:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail=USER_NOT_FOUND)

    elif role == 'Supervisor':
        users = get_supervisor(current_user)
        if users:
            return users
        else:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail=USER_NOT_FOUND)

    else:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail=USER_UNAUTHORIZED)


def getting_users_by_id(id, current_user):
    role = role_power(current_user.id)

    if role == 'SuperAdmin':
        user = get_user_id(id)
        if user:
            return user
        else:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail=USER_NOT_FOUND)

    elif role == 'Admin':
        user = get_admin_id(id, current_user)
        if user:
            return user
        else:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail=USER_NOT_FOUND)

    elif role == 'Supervisor':
        user = get_supervisor_id(id, current_user)
        if user:
            return user
        else:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail=USER_NOT_FOUND)

    else:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail=USER_UNAUTHORIZED)
