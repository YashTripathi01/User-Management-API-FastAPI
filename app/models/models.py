from ..database.database import Base
from sqlalchemy import Column, ForeignKey, String, Integer, Date, TIMESTAMP


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(254), nullable=False, unique=True)
    password = Column(String(500), nullable=False)
    contact_no = Column(String(20), nullable=False)
    working_under = Column(Integer, nullable=False)
    dob = Column(Date, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    is_active = Column(Integer, nullable=False)
    updated_at = Column(TIMESTAMP)
    co_id = Column(Integer, ForeignKey('company.company_id'))
    role_id = Column(Integer, ForeignKey('role.role_id'))


class Company(Base):
    __tablename__ = 'company'

    company_id = Column(Integer, primary_key=True, nullable=False)
    company_name = Column(String(100), unique=True, nullable=False)
    country = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    pin_code = Column(String(20), nullable=False)
    department = Column(String(50), nullable=False)
    branch = Column(String(100), nullable=False)
    address = Column(String(250), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP)
    is_active = Column(Integer, nullable=False)


class Role(Base):
    __tablename__ = 'role'

    role_id = Column(Integer, primary_key=True, nullable=False)
    role_power = Column(String(10), unique=True, nullable=False)
