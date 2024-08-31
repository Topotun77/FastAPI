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
from models.task import Task
from models.user import User
from schemas import CreateUser, UpdateUser, CreateTask, UpdateTask


router_task = APIRouter(prefix='/task', tags=['task'])


@router_task.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    task = db.scalars(select(Task)).all()
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Ничего нет'
        )
    return task


@router_task.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)],
                     task_id: Annotated[int, Query(ge=1, le=1000, description='Введите ID задачи', example=1)]):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Задача с таким ID не найдена'
        )
    return task

@router_task.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)],
                      create_tsk: CreateTask,
                      user_id: Annotated[int, Query(ge=1, le=120, description='Введите ID пользователя', example=1)]):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Пользователь с таким ID не найден'
        )
    db.execute(insert(Task).values(
        title=create_tsk.title,
        content=create_tsk.content,
        priority=create_tsk.priority,
        user_id=user_id,
        slug=create_tsk.title.lower()+'_'+str(create_tsk.priority)
    ))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Добавление задачи выполнено успешно'
    }

@router_task.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)],
                      update_tsk: UpdateTask,
                      task_id: Annotated[int, Query(ge=1, le=120, description='Введите ID задачи', example=1)]):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Задача с таким ID не найдена')
    db.execute(update(Task).where(Task.id == task_id).values(
        title=update_tsk.title,
        content=update_tsk.content,
        priority=update_tsk.priority,
    ))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Обновление выполнено успешно'
    }


@router_task.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)],
                      task_id: Annotated[int, Query(ge=1, le=120, description='Введите ID задачи', example=1)]):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Задача с таким ID не найдена')
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Задача успешно удалена'
    }
