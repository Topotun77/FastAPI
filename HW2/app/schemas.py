from pydantic import BaseModel, Field

class CreateUser(BaseModel):
    username: str = Field(default='User', min_length=3, max_length=15, description='Введите псевдоним',
                          example='User')
    firstname: str = Field(default='Alex', min_length=3, max_length=15, description='Введите имя пользователя',
                           example='Alex')
    lastname: str = Field(default='Ivanov', min_length=3, max_length=15, description='Введите фамилию пользователя',
                          example='Ivanov')
    age: int = Field(default=21, ge=18, le=120, description='Введите возраст', example=22)


class UpdateUser(BaseModel):
    username: str = Field(default='User', min_length=3, max_length=15, description='Введите псевдоним',
                          example='User')
    firstname: str = Field(default='Alex', min_length=3, max_length=15, description='Введите имя пользователя',
                           example='Alex')
    lastname: str = Field(default='Ivanov', min_length=3, max_length=15, description='Введите фамилию пользователя',
                          example='Ivanov')
    age: int = Field(default=21, ge=18, le=120, description='Введите возраст', example=22)


class CreateTask(BaseModel):
    title: str
    content: str
    priority: int


class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int
