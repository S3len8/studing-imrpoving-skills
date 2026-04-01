from typing import Callable
from functools import wraps

error_counter_success = 0


def retry_on_exception(retries: int):
    def wrapper(func: Callable):
        @wraps(func)
        def inner(*args, **kwargs):
            i = 1
            while i <= retries:
                try:
                    result = func(*args, **kwargs)
                    print(f"ok")
                    i += 1
                    return result
                except Exception as e:
                    if i < retries:
                        print(f"{type(e).__name__}")
                    else:
                        print(f"final {type(e).__name__}")
                    i += 1
        return inner
    return wrapper


@retry_on_exception(retries=3)
def test_success_after_one_fail():
    global error_counter_success
    if error_counter_success < 2:
        error_counter_success += 1
        raise ValueError
    return "Success after fail!"


@retry_on_exception(retries=3)
def test_fail_all_attempts():
    raise AttributeError


@retry_on_exception(retries=3)
def test_success_immediately():
    return "Success Immediately!"


test_success_immediately()
test_fail_all_attempts()
test_success_after_one_fail()