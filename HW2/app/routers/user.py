from fastapi import APIRouter
from HW2.app.backend.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
# from HW2.app.routers.task import Task
from HW2.app.schemas import CreateUser

router_user = APIRouter(prefix='/user', tags=['user'])


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    tasks = relationship('Task', back_populates='user')


from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))


@router_user.get('/')
async def all_users():
    pass


@router_user.get('/user_id')
async def user_by_id(user_id: int) -> CreateUser:
    pass


@router_user.post('/create')
async def create_user():
    pass


@router_user.put('/update')
async def update_user():
    pass


@router_user.delete('/delete')
async def delete_user():
    pass
