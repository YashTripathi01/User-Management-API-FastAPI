from .database.database import session
from .helpers.hash import hash
from .models.models import Company
import datetime

db = session


def initial_setup():
    password = hash('12345678')
    to_execute = db.query(Company).get(0)

    if not to_execute:
        add_com = f'insert into company(company_id, company_name, country, state, city, pin_code, department, branch, address, created_at, updated_at, is_active) values(0, "SuperCompany", "SuperCompany", "SuperCompany", "SuperCompany", "123456", "SuperCompany", "SuperCompany", "SuperCompany", "{datetime.datetime.now()}", "{datetime.datetime.now()}", 1);'
        db.execute(add_com)
        db.commit()

        update_com = 'update company set company_id = 0 where company_id = 1'
        db.execute(update_com)
        db.commit()

        add_role = f'insert into role(role_id, role_power) values(0, "SuperAdmin")'
        db.execute(add_role)
        db.commit()

        update_role = 'update role set role_id = 0 where role_id = 1'
        db.execute(update_role)
        db.commit()

        add_roles = 'insert into role (role_id, role_power) values(1, "Admin"), (2, "Supervisor"), (3, "User")'
        db.execute(add_roles)
        db.commit()

        add_user = f'insert into users (first_name, last_name, email, password, contact_no, working_under, dob, created_at, is_active, updated_at, co_id, role_id) values("SuperAdmin", "SuperAdmin", "super@admin.com", "{password}", "1234567890", 0, "2022-06-03", "{datetime.datetime.now()}", 1, "{datetime.datetime.now()}", 0, 0)'
        db.execute(add_user)
        db.commit()
        print('Initial SetUp Successful!')

    else:
        print('Initial SetUp Already Done!')
