from fastapi import HTTPException
from http import HTTPStatus
from ...config.error_logs import *
from ...helpers.database_helper import if_user_exists, list_company_id, role_power, add_new_user
from ...schemas.user_schema import UserPydantic, UserResponse


def adding_user(request: UserPydantic, current_user: UserResponse):
    role = role_power(current_user.id)
    if role == 'User':
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail=USER_UNAUTHORIZED)

    already_exists = if_user_exists(request=request)
    if already_exists:
        raise HTTPException(status_code=HTTPStatus.CONFLICT,
                            detail=USER_ALREADY_EXISTS)

    company_id = list_company_id()

    if request.co_id not in company_id:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail=COMPANY_NOT_FOUND)

    check_working_under = role_power(request.working_under)

    if role == 'SuperAdmin':
        if request.role_id in [1, 2, 3]:
            if request.role_id == 3:
                if check_working_under == 'Supervisor':
                    add_new_user(request=request)
                    return HTTPException(status_code=HTTPStatus.CREATED, detail=ADD_USER)
                else:
                    return HTTPException(status_code=HTTPStatus.FORBIDDEN, detail=WORKING_UNDER_IS_NOT_A_SUPERVISOR)

            elif request.role_id == 2:
                if check_working_under == 'Admin':
                    add_new_user(request=request)
                    return HTTPException(status_code=HTTPStatus.CREATED, detail=ADD_USER)
                else:
                    return HTTPException(status_code=HTTPStatus.FORBIDDEN, detail=WORKING_UNDER_IS_NOT_A_ADMIN)

            elif request.role_id == 1:
                request.working_under == 1
                add_new_user(request=request)
                return HTTPException(status_code=HTTPStatus.CREATED, detail=ADD_USER)
        else:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST, detail=INVALID_ROLE)

    elif role == 'Admin':
        request.co_id = current_user.co_id
        if request.role_id in [2, 3]:
            if request.role_id == 3:
                if check_working_under == 'Supervisor':
                    request.co_id = current_user.co_id
                    add_new_user(request=request)
                    return HTTPException(status_code=HTTPStatus.CREATED, detail=ADD_USER)
                else:
                    return HTTPException(status_code=HTTPStatus.FORBIDDEN, detail=WORKING_UNDER_IS_NOT_A_SUPERVISOR)

            elif request.role_id == 2:
                if check_working_under == 'Admin':
                    add_new_user(request=request)
                    return HTTPException(status_code=HTTPStatus.CREATED, detail=ADD_USER)
                else:
                    return HTTPException(status_code=HTTPStatus.FORBIDDEN, detail=WORKING_UNDER_IS_NOT_A_SUPERVISOR)

        else:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST, detail=INVALID_ROLE)

    elif role == 'Supervisor':
        request.co_id = current_user.co_id
        if request.role_id in [3]:
            if request.role_id == 3:
                if check_working_under == 'Supervisor' and current_user.co_id == request.co_id:
                    add_new_user(request=request)
                    return HTTPException(status_code=HTTPStatus.CREATED, detail=ADD_USER)
                else:
                    return HTTPException(status_code=HTTPStatus.FORBIDDEN, detail=WORKING_UNDER_IS_NOT_A_SUPERVISOR)

            else:
                raise HTTPException(
                    status_code=HTTPStatus.BAD_REQUEST, detail=INVALID_ROLE)

        else:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST, detail=INVALID_ROLE)

    else:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED)
