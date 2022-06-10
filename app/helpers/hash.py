from werkzeug.security import generate_password_hash, check_password_hash


# generate password hash
def hash(password: str):
    print('==hash==')
    return generate_password_hash(password)


# verify password
def verify_hash(hashed_password, plain_password):
    return check_password_hash(hashed_password, plain_password)
