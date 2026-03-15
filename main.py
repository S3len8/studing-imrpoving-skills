from pydantic import BaseModel, Field, EmailStr, ConfigDict
from fastapi import FastAPI
import uvicorn

app = FastAPI()

user = {
        'email': 'email@gmail.com',
        'bio': "User",
        'age': 12,
    }


def func(user_: dict): # Функція яка виконує певні дії з даними словника
    user_['age'] += 1


class UserSchema(BaseModel): # Створення схеми з наслідуванням до BaseModel
    email: EmailStr # Валідація для емейлу
    bio: str | None = Field(max_length=10) # Валідація для біо
    # age: int = Field(ge=0, le=99999999999999999999) # Валідація для віку
    model_config = ConfigDict(extra='forbid')


class UserAgeSchema(UserSchema): # Створення схеми з наслідуванням до UserSchema
    age: int = Field(ge=0, le=99999999999999999999) # Валідація для віку


users = []


@app.post("/users")
def add_user(user: UserSchema):
    users.append(user)
    return {"ok": True, "msg": "Користувач доданий"}


@app.get("/users")
def get_user():
    return users


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
    print(UserAgeSchema(**user))
    print(UserSchema(**user)) # Розкриття даних з словнику як **kwargs