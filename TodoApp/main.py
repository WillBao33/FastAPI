from fastapi import FastAPI, Request
from .models import Base
from .database import engine
from .routers import auth, todos, admin, users
from fastapi.staticfiles import StaticFiles
from fastapi import status
from fastapi.responses import RedirectResponse

app = FastAPI()

Base.metadata.create_all(bind=engine) # this creates everything from database.py and models.py, but it won't run if this todos.db already exists


app.mount("/static", StaticFiles(directory="TodoApp/static"), name='static')


@app.get('/')
def test(request: Request):
    return RedirectResponse(url="/todos/todo-page", status_code=status.HTTP_302_FOUND)


@app.get("/healthy")
def health_check():
    return {'status': 'healthy'}



app.include_router(auth.router)
app.include_router(todos.router)

app.include_router(admin.router)

app.include_router(users.router)