from fastapi import APIRouter
from schemas import CreateUser

router_user = APIRouter(prefix='/user', tags=['user'])


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
