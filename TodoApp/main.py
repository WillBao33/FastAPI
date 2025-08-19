from fastapi import FastAPI
import models
import routers
from database import engine
from routers import auth, todos, admin, users

app = FastAPI()

models.Base.metadata.create_all(bind=engine) # this creates everything from database.py and models.py, but it won't run if this todos.db already exists


app.include_router(auth.router)
app.include_router(todos.router)

app.include_router(admin.router)

app.include_router(users.router)