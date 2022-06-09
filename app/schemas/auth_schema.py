from dataclasses import field
from pydantic import BaseModel, EmailStr
from marshmallow import Schema, fields
from typing import List, Optional


class LoginPydantic(BaseModel):
    email: Optional[EmailStr]
    password: Optional[str]


class LoginMarsh(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)


class ResetPassPydantic(BaseModel):
    email: List[Optional[EmailStr]]


class ResetPassMarsh(Schema):
    email = fields.List(fields.Email(required=True))


class TokenDataPydantic(BaseModel):
    email: Optional[str] = None
