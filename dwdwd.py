from typing import Callable
from functools import wraps

def add_tag(tag: str):
    def wrapper(func: Callable):
        @wraps(func)
        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            return f"<{tag}>{res}</{tag}>"
        return inner
    return wrapper

def add_div(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return f"<div>{res}</div>"
    return wrapper

@add_tag("h2")
def greeting(name: str) -> str:
    return f"Hello, {name}!"

print(greeting("Anton"))  # <h2>Hello, Anton!</h2>

@add_div
def greeting(name: str) -> str:
    return f"Hello, {name}!"

print(greeting("Grisha"))  # <div>Hello, Grisha!</div>

@add_tag("h2")
@add_div
def greeting(name: str) -> str:
    return f"Hello, {name}!"

print(greeting("Maksim"))  # <h2><div>Hello, Maksim!</div></h2>