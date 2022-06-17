from fastapi import HTTPException
from http import HTTPStatus
from ...helpers import hash, oauth, database_helper
from ...config.error_logs import *


def login_user(request):
    user = database_helper.login_email_check(request=request)

    if user is None:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail=INVALID_CREDENTIALS)

    if not user.is_active == 1:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail=USER_INACTIVE)

    if not user:
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN,
                            detail=INVALID_CREDENTIALS)

    if not hash.verify_hash(user.password, request.password):
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail=INVALID_CREDENTIALS)

    access_token = oauth.create_access_token(data={'id': user.id, 'email': user.email, 'co_id': user.co_id, 'first_name': user.first_name,
                                             'last_name': user.last_name, 'role_id': user.role_id, 'contact_no': user.contact_no, 'working_under': user.working_under, 'company_id': user.co_id})

    return {'access_token': access_token, 'token_type': 'bearer', 'message': LOGIN}
