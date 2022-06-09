from fastapi import HTTPException
from http import HTTPStatus
from ...config.error_logs import *
from ...helpers.database_helper import email_check, list_company_id, role_power, get_user_id, update_user
from ...schemas.user_schema import UserUpdatePydantic, UserResponse


def updating_user(id: int, request: UserUpdatePydantic, current_user: UserResponse):
    role = role_power(current_user.id)
    if role == 'User':
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail=USER_UNAUTHORIZED)

    email_already_exists = email_check(id=id)

    if request.email in email_already_exists:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT, detail=EMAIL_FOUND)

    company_id = list_company_id()

    if request.co_id not in company_id:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail=COMPANY_NOT_FOUND)

    user_to_update = get_user_id(id=id)

    if not user_to_update:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail=USER_NOT_FOUND)

    if role == 'SuperAdmin':
        if request.role_id in [1, 2, 3] and current_user.role_id < user_to_update.role_id:
            if request.role_id == 3:
                check_bool = role_power(request.working_under)
                if check_bool == 'Supervisor':
                    update_user(request=request, id=id)
                    return HTTPException(status_code=HTTPStatus.CREATED, detail=UPDATE_USER)
                else:
                    return HTTPException(status_code=HTTPStatus.FORBIDDEN, detail=WORKING_UNDER_IS_NOT_A_SUPERVISOR)

            elif request.role_id == 2:
                check_bool = role_power(request.working_under)
                if check_bool == 'Admin':
                    update_user(request=request, id=id)
                    return HTTPException(status_code=HTTPStatus.CREATED, detail=UPDATE_USER)

                else:
                    return HTTPException(status_code=HTTPStatus.FORBIDDEN, detail=WORKING_UNDER_IS_NOT_A_ADMIN)

            elif request.role_id == 1:
                request.working_under = current_user.id
                update_user(request=request, id=id)
                return HTTPException(status_code=HTTPStatus.CREATED, detail=UPDATE_USER)

        else:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST, detail=INVALID_ROLE)

    elif role == 'Admin':
        if current_user.co_id == user_to_update.co_id:
            if current_user.role_id < user_to_update.role_id:
                if request.role_id in [2, 3] and current_user.co_id == current_user.co_id:
                    if request.role_id == 3:
                        check_bool = role_power(request.working_under)
                        if check_bool == 'Supervisor':
                            update_user(request=request, id=id)
                            return HTTPException(status_code=HTTPStatus.CREATED, detail=UPDATE_USER)
                        else:
                            return HTTPException(status_code=HTTPStatus.FORBIDDEN, detail=WORKING_UNDER_IS_NOT_A_SUPERVISOR)

                    elif request.role_id == 2:
                        check_bool = role_power(request.working_under)
                        if check_bool == 'Admin':
                            update_user(request=request, id=id)
                            return HTTPException(status_code=HTTPStatus.CREATED, detail=UPDATE_USER)
                        else:
                            return HTTPException(status_code=HTTPStatus.FORBIDDEN, detail=WORKING_UNDER_IS_NOT_A_ADMIN)

                else:
                    raise HTTPException(
                        status_code=HTTPStatus.BAD_REQUEST, detail=INVALID_ROLE)

            else:
                raise HTTPException(
                    status_code=HTTPStatus.UNAUTHORIZED, detail=USER_UNAUTHORIZED)

        else:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED, detail=USER_UNAUTHORIZED)

    elif role == 'Supervisor':
        if current_user.co_id == user_to_update.co_id:
            if request.role_id in [3] and current_user.role_id < user_to_update.role_id and request.co_id == current_user.co_id:
                if request.role_id == 3:
                    check_bool = role_power(request.working_under)
                    if check_bool == 'Supervisor':
                        update_user(request=request, id=id)
                        return HTTPException(status_code=HTTPStatus.CREATED, detail=UPDATE_USER)
                    else:
                        return HTTPException(status_code=HTTPStatus.FORBIDDEN, detail=WORKING_UNDER_IS_NOT_A_SUPERVISOR)

                else:
                    raise HTTPException(
                        status_code=HTTPStatus.FORBIDDEN, detail=INVALID_ROLE)

            else:
                raise HTTPException(
                    status_code=HTTPStatus.UNAUTHORIZED, detail=USER_UNAUTHORIZED)

        else:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED, detail=USER_UNAUTHORIZED)

    else:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail=USER_UNAUTHORIZED)
