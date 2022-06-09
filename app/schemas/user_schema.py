from pydantic import BaseModel, EmailStr
from marshmallow import Schema, fields
from typing import Optional


# schema for adding user pydantic
class UserPydantic(BaseModel):
    co_id: Optional[int]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    role_id: Optional[int]
    contact_no: Optional[str]
    working_under: Optional[int]
    dob: Optional[str]

    class Config:
        orm_mode = True


# schema for adding user marshmallow
class UserMarsh(Schema):
    co_id = fields.Integer(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    role_id = fields.Integer(required=True)
    contact_no = fields.String(required=True)
    working_under = fields.Integer(required=True)
    dob = fields.Date(required=True)


# schema for updating user pydantic
class UserUpdatePydantic(BaseModel):
    co_id: Optional[int]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    role_id: Optional[int]
    contact_no: Optional[str]
    working_under: Optional[int]
    dob: Optional[str]

    class Config:
        orm_mode = True


# schema for updating user marsh
class UserUpdateMarsh(Schema):
    co_id = fields.Integer(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(required=True)
    contact_no = fields.String(required=True)
    role_id = fields.Integer(required=True)
    working_under = fields.Integer(required=True)
    dob = fields.Date(required=True)


# schema for user response pydantic
class UserResponse(BaseModel):
    first_name: str
    last_name: str
    email: str
    contact_no: str
    working_under: str
    role_id: int
    co_id: int

    class Config:
        orm_mode = True
