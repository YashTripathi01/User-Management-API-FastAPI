import datetime
from sqlalchemy import and_, delete, select
from ..models.models import Users, Company
from ..database.database import session
from ..helpers.hash import hash

db = session


##### LOGIN #####
def login_email_check(request):
    return db.query(Users).filter(Users.email == request.email).first()


##### RESET PASSWORD #####
def update_password(hashed_password, email):
    # query = f'update users set password = "{hashed_password}" where email = "{email}"'
    # db.execute(query)
    # db.commit()
    # db.close()
    db.query(Users).filter(Users.email == email).update(
        {'password': hashed_password})
    db.commit()


##### USERS #####
def role_power(id):
    query = f'SELECT role_power FROM role INNER JOIN users on role.role_id = users.role_id where id = {id}'
    res = db.execute(query).fetchall()

    if res != []:
        for i in res:
            return i[0]
    else:
        return {'message': f'No user exists with the id {id}'}


def if_user_exists(request):
    return db.query(Users).filter(Users.email == request.email).first()


def add_new_user(request):
    new_password = hash(request.password)
    request.password = new_password
    new_user = Users(
        is_active=1, created_at=datetime.datetime.now(), **request.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()


def update_user(request, id):
    # query = f'update users set co_id = {request.co_id}, first_name = "{request.first_name}", last_name = "{request.last_name}", email = "{request.email}", contact_no = "{request.contact_no}", working_under = {request.working_under}, dob = "{request.dob}", role_id = "{request.role_id}", updated_at = "{datetime.datetime.now()}"  where id = {id}'
    # db.execute(query)
    # db.commit()
    # db.close()
    db.query(Users).filter(Users.id == id).update({'co_id': request.co_id, 'first_name': request.first_name, 'last_name': request.last_name, 'email': request.email,
                                                   'contact_no': request.contact_no, 'working_under': request.working_under, 'dob': request.dob, 'role_id': request.role_id, 'updated_at': datetime.datetime.now()})
    db.commit()
    db.close()


def get_all_user():
    return db.query(Users).all()


def get_user_id(id: int):
    return db.query(Users).get(id)


def get_admin_id(id: int, current_user):
    query = f'SELECT * FROM users WHERE id = {id} AND role_id != 0 AND co_id = {current_user.co_id}'
    # query = select(Users).where(
    #     and_(Users.role_id != 0, Users.id == f'{id}', Users.co_id==f'{current_user.co_id}'))

    return db.execute(query).fetchone()


def get_admin(current_user):
    query = f'SELECT * FROM users WHERE role_id != 0 AND co_id = {current_user.co_id}'

    return db.execute(query).fetchall()


def get_supervisor_id(id: int, current_user):
    query = f'SELECT * FROM users WHERE id = {id} AND role_id != 0 AND role_id != 1 AND co_id = {current_user.co_id}'

    return db.execute(query).fetchone()


def get_supervisor(current_user):
    query = f'SELECT * FROM users WHERE role_id != 0 AND role_id != 1 AND co_id = {current_user.co_id}'

    return db.execute(query).fetchall()


def email_check(id: int):
    # query = f'SELECT email from users WHERE id != "{id}"'
    query = select(Users.email).where(id != f'{id}')

    return db.execute(query).fetchall()


def delete_super_admin(id):
    try:
        # query = f'DELETE FROM users WHERE id = {id}'
        # db.execute(query)
        db.query(Users).filter(Users.id == f'{id}').delete()
        db.commit()
        db.close()
        return True
    except:
        return False


def delete_admin(id):
    try:
        # query = f'DELETE FROM users WHERE id = {id} AND role_id != 0 AND role_id != 1'
        # db.execute(query)
        db.query(Users).filter(
            Users.id == f'{id}', Users.role_id != 0, Users.role_id != 1).delete()
        db.commit()
        db.close()
        return True
    except:
        return False


def delete_supervisor(id):
    try:
        # query = f'DELETE FROM users WHERE id = {id} AND role_id != 0 AND role_id != 1 AND role_id != 2'
        # db.execute(query)
        print('doe')
        db.query(Users).filter(
            Users.id == f'{id}', Users.role_id != 0, Users.role_id != 1, Users.role_id != 2).delete()
        db.commit()
        db.close()
        return True
    except:
        return False


def get_supervisor_super_admin():
    query = f'SELECT * FROM users WHERE role_id = 2'
    return db.execute(query).fetchall()


def get_supervisor_admin_supervisor(co_id):
    query = f'SELECT * FROM users WHERE role_id = 2 AND co_id = {co_id}'
    return db.execute(query).fetchall()


##### COMPANY #####
def list_company_id():
    company_id = db.query(Company).with_entities(Company.company_id)
    id_list = []

    for id in company_id:
        id_list.append(id[0])

    return id_list


def valid_company_name(company_name: str):
    return db.query(Company).filter(Company.company_name == company_name).first()


def add_new_company(request):
    new_company = Company(
        is_active=1, created_at=datetime.datetime.now(), **request.dict())
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    db.close()


def get_all_companies():
    return db.query(Company).all()


def get_companies_by_id(id: int):
    return db.query(Company).get(id)


def delete_company(id: int):
    # query = f'UPDATE company SET is_active = 0 WHERE company_id = {id}'
    # db.execute(query)
    # db.commit()
    db.query(Company).filter(Company.company_id ==
                             f'{id}').update({'is_active': 0})
    db.commit()

    # new_query = f'UPDATE users set is_active = 0 WHERE co_id = {id}'
    # db.execute(new_query)
    db.query(Users).filter(Users.co_id == f'{id}').update({'is_active': 0})
    db.commit()
    db.close()


def update_company(id: int, request):
    # query = f'update company set company_name="{request.company_name}", country="{request.country}", state ="{request.state}", city = "{request.city}", pin_code = "{request.pin_code}", department = "{request.department}", branch = "{request.branch}", address = "{request.address}", updated_at = "{datetime.datetime.now()}" where company_id = {id}'
    # db.execute(query)
    db.query(Company).filter(Company.company_id == id).update({'company_name': request.company_name, 'country': request.country, 'state': request.state, 'city': request.city,
                                                               'pin_code': request.pin_code, 'department': request.department, 'branch': request.branch, 'address': request.address, 'updated_at': datetime.datetime.now()})
    db.commit()
    db.close()
