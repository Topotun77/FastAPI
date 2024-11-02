from fastapi import FastAPI
from routers import task, user
# from schemas import CreateUser, CreateTask

app = FastAPI()


@app.get('/')
async def start() -> dict:
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router_task)
app.include_router(user.router_user)
