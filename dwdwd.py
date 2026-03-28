def my_range(*args: int, **kwargs: int) -> int:
    if len(args) == 1:
        start = 0
        stop = args[0]
        step = 1
        while stop > start:
            yield start
            start += step
    if len(args) == 2:
        start = args[0]
        stop = args[1]
        step = 1
        while stop > start:
            yield start
            start += step
    if len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
        if step > 0:
            while stop > start:
                yield start
                start += step
        if step < 0:
            while start > stop:
                yield start
                start += step
        if step == 0:
            raise ValueError


range = my_range(9)
print(list(range))