from pydantic import BaseModel
from marshmallow import Schema, fields
from typing import Optional


class CompanyPydantic(BaseModel):
    company_name: Optional[str]
    country: Optional[str]
    state: Optional[str]
    city: Optional[str]
    pin_code: Optional[str]
    department: Optional[str]
    branch: Optional[str]
    address: Optional[str]

    class Config:
        orm_mode = True


class CompanyMarsh(Schema):
    company_name = fields.String(required=True)
    country = fields.String(required=True)
    state = fields.String(required=True)
    city = fields.String(required=True)
    pin_code = fields.String(required=True)
    department = fields.String(required=True)
    branch = fields.String(required=True)
    address = fields.String(required=True)


class CompanyResponse(BaseModel):
    company_id: int
    company_name: str
    country: str
    state: str
    city: str
    pin_code: str
    department: str
    branch: str
    address: str
    is_active: int

    class Config:
        orm_mode = True
