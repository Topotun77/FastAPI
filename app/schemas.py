from pydantic import BaseModel, Field

class CreateUser(BaseModel):
    username: str = Field(default='User1', min_length=3, max_length=15, description='Введите псевдоним',
                          example='User')
    firstname: str = Field(default='Pasha', min_length=3, max_length=15, description='Введите имя пользователя',
                           example='Alex')
    lastname: str = Field(default='Durov', min_length=3, max_length=15, description='Введите фамилию пользователя',
                          example='Ivanov')
    age: int = Field(default=39, ge=18, le=120, description='Введите возраст', example=22)


class UpdateUser(BaseModel):
    firstname: str = Field(default='Bear', min_length=3, max_length=15, description='Введите имя пользователя',
                           example='Alex')
    lastname: str = Field(default='Grylls', min_length=3, max_length=15, description='Введите фамилию пользователя',
                          example='Ivanov')
    age: int = Field(default=50, ge=18, le=120, description='Введите возраст', example=22)


class CreateTask(BaseModel):
    title: str = Field(default='FirstTask', min_length=3, max_length=10, description='Введите имя задачи',
                       example='Sleep')
    content: str = Field(default='Content1', min_length=3, max_length=10, description='Введите содержание задачи',
                         example='Sleep')
    priority: int = Field(default=0, ge=0, le=10, description='Введите приоритет', example=5)


class UpdateTask(BaseModel):
    title: str = Field(default='FirstTask', min_length=3, max_length=10, description='Введите имя задачи',
                       example='Sleep')
    content: str = Field(default='Content1', min_length=3, max_length=10, description='Введите содержание задачи',
                         example='Sleep')
    priority: int = Field(default=0, ge=0, le=10, description='Введите приоритет', example=5)
