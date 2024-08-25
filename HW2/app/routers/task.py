from fastapi import APIRouter
from HW2.app.backend.db import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from HW2.app.routers.user import User
from HW2.app.schemas import CreateTask

# from .user import User

router_task = APIRouter(prefix='/task', tags=['task'])


class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), index=True, nullable=True)
    slug = Column(String, unique=True, index=True)

    user = relationship('User', back_populates='tasks')


from sqlalchemy.schema import CreateTable
print(CreateTable(Task.__table__))


@router_task.get('/')
async def all_tasks():
    pass


@router_task.get('/task_id')
async def task_by_id(task_id: int) -> CreateTask:
    pass


@router_task.post('/create')
async def create_task():
    pass


@router_task.put('/update')
async def update_task():
    pass


@router_task.delete('/delete')
async def delete_task():
    pass
