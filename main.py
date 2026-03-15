from pydantic import BaseModel

user = {
        'email': 'email@gmail',
        'bio': "User",
        'age': 12,
    }


def func(user_: dict): # Функція яка виконує певні дії з даними словника
    user_['age'] += 1


class UserSchema(BaseModel): # Створення схеми з наслідуванням до BaseModel
    email: str # Валідація для емейлу
    bio: str | None # Валідація для біо
    age: int # Валідація для віку


print(UserSchema(**user)) # Розкриття даних з словнику як **kwargs