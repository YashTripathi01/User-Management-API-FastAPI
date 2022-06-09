import string
import random
from fastapi_mail import MessageSchema, ConnectionConfig, FastMail
from fastapi import HTTPException
from http import HTTPStatus
from .constants import *
from ...helpers.database_helper import update_password
from ...helpers import hash
from ...config.error_logs import *


async def reset_user_password(request):
    if not request.email:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail=EMAIL_NOT_FOUND)

    letters = string.ascii_lowercase
    new_password = ''.join(random.choice(letters) for i in range(8))
    hashed_password = hash.hash(new_password)
    update_password(hashed_password=hashed_password, email=request.email)

    email = request.email
    conf = ConnectionConfig(
        MAIL_USERNAME=MAIL_USERNAME,
        MAIL_PASSWORD=PASSWORD,
        MAIL_FROM=MAIL_FROM,
        MAIL_PORT=587,
        MAIL_SERVER="smtp.gmail.com",
        MAIL_FROM_NAME="OI-Analytics",
        MAIL_TLS=True,
        MAIL_SSL=False,
        USE_CREDENTIALS=True,
        VALIDATE_CERTS=True
    )
    message = MessageSchema(
        subject="Reset Password",
        recipients=email,
        body=f'New Password is {new_password}',
    )
    fm = FastMail(conf)
    await fm.send_message(message)
    raise HTTPException(status_code=HTTPStatus.OK,
                        detail='Mail sent Successfully')
