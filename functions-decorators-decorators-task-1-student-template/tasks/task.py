import time
from typing import Dict

execution_time: Dict[str, float] = {}


def time_decorator(decorated_func):
    def wrapper(*args):
        start = time.time()
        res = decorated_func(*args)
        end = time.time()
        execution_time.update({decorated_func.__name__: end - start})
        return res

    return wrapper


@time_decorator
def get_sum(a, b):
    time.sleep(0.4)
    return a + b


@time_decorator
def get_multiply(a, b):
    time.sleep(0.3)
    return a * b


if __name__ == '__main__':
    res1 = get_sum(10, 20)
    print(f"res1: {res1}")

    res2 = get_multiply(35, 788)
    print(f"res2: {res2}")

    res3 = get_sum(87, 334)
    print(f"res3: {res3}")

    print(execution_time)
