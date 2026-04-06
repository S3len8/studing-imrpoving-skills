# def deco():
#     ...
#
#
# @deco # Перший варіант як можна застосувати декоратор синтаксичний цукор
# def my_func():
#     return 123
#
#
# my_func = deco(my_func) # Другий варіант як можна створити декоратор
# from collections.abc import Callable
#
#
# def empty_deco(func: Callable):
#     def wrapper():
#         res = func()
#         return res
#     return wrapper
#
# @empty_deco
# def my_func():
#     return 123
#
# print(my_func())

# from collections.abc import Callable
# import time
#
# def timer_deco(func: Callable):
#     def wrapper():
#         start = time.perf_counter()
#         res = func()
#         end = time.perf_counter()
#         print(f"Виконання зайняло: {end-start}")
#         return res
#     return wrapper
#
# @timer_deco
# def my_func():
#     time.sleep(1)
#     return 123
#
# print(my_func())


# from collections.abc import Callable
# import time
#
# def param_timer_deco(func: Callable):
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         res = func(*args, **kwargs)
#         end = time.perf_counter()
#         print(f"Виконання зайняло: {end-start}")
#         return res
#     return wrapper
#
# @param_timer_deco
# def my_func(sleep_time: int):
#     time.sleep(sleep_time)
#     return 123
#
# print(my_func(3))


# from collections.abc import Callable
# import time
# from functools import wraps
#
# def limit_calls(limit: int):
#     def wrapper(func: Callable):
#         @wraps(func)
#         def inner(*args, **kwargs):
#             """Лол другий докстрінг тримай"""
#             nonlocal limit
#             if limit == 0:
#                 print("Неможна користуватися функцією")
#                 return
#
#             res = func(*args, **kwargs)
#             limit -= 1
#             return res
#         return inner
#     return wrapper
#
#
# @limit_calls(2)
# def my_func(sleep_time: int):
#     """Дуже важливий докстірнг не загуби"""
#     time.sleep(sleep_time)
#     return 123
#
# print(my_func.__doc__)
# print(my_func.__name__)


import time
# from functools import wraps
# from typing import Coroutine
# import asyncio
#
#
# def deco(coroutine: Coroutine):
#     @wraps(coroutine)
#     async def wrapper(*args, **kwargs):
#         res = await coroutine(*args, **kwargs)
#         return res
#     return wrapper
#
#
# @deco
# async def async_my_func():
#     """Дуже важливий докстірнг не загуби"""
#     await asyncio.sleep(0.5)
#     return 123
#
#
# print(asyncio.run(async_my_func()))


from typing import Callable
from functools import wraps

def log_func(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"func: {func.__name__}, args: {args}, kwargs: {kwargs}")
        res = func(*args, **kwargs)
        return res
    return wrapper 

