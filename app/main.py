from fastapi import FastAPI
from .database.database import engine
from .models import models
from .routes.authentication import login, reset_password
from .routes.users import add_user, get_user, update_user, delete_user, get_supervisor
from .routes.company import add_company, get_company, update_company, delete_company

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(login.router)
app.include_router(reset_password.router)

app.include_router(add_user.router)
app.include_router(get_user.router)
app.include_router(update_user.router)
app.include_router(delete_user.router)
app.include_router(get_supervisor.router)

app.include_router(add_company.router)
app.include_router(get_company.router)
app.include_router(update_company.router)
app.include_router(delete_company.router)


@app.get('/')
def root():
    return {'message': 'Hello, World!'}
