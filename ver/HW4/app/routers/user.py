from fastapi import APIRouter, Depends, status, HTTPException, Path, Query
# from pydantic import Field
# Сессия БД
from sqlalchemy.orm import Session
# Аннотации, Модели БД и Pydantic.
from typing import Annotated, Dict
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify

# Функция подключения к БД
from backend.db_depends import get_db
from models.user import User
from schemas import CreateUser, UpdateUser, CreateTask, UpdateTask

router_user = APIRouter(prefix='/user', tags=['user'])


@router_user.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    if users is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Ничего нет'
        )
    return users

@router_user.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)],
                     user_id: Annotated[int, Query(ge=1, le=120, description='Введите ID пользователя', example=1)]):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Нет такого пользователя'
        )
    return user


@router_user.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], create_usr: CreateUser) -> dict:
    user = db.scalar(select(User).where(User.username == create_usr.username))
    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Такой пользователь уже существует'
        )
    db.execute(insert(User).values(username=create_usr.username,
                                   firstname=create_usr.firstname,
                                   lastname=create_usr.lastname,
                                   age=create_usr.age))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Пользователь успешно добавлен'
    }


@router_user.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)], update_usr: UpdateUser,
                      user_id: Annotated[int, Query(ge=1, le=120, description='Введите ID пользователя', example=1)]):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Такого пользователя не существует'
        )
    db.execute(update(User).where(User.id == user_id).values(firstname=update_usr.firstname,
                                                             lastname=update_usr.lastname,
                                                             age=update_usr.age))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Обновление выполнено успешно'
    }


@router_user.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)],
                      user_id: Annotated[int, Query(ge=1, le=120, description='Введите ID пользователя', example=1)]):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Такого пользователя не существует'
        )
    db.execute(delete(User).where(User.id == user_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Удаление выполнено успешно'
    }
