from functools import wraps


def decorator_apply(lambda_func):
    def decorator_func(decorated_func):
        @wraps(decorated_func)
        def wrapper(*args, **kwargs):
            res = decorated_func(*args, **kwargs)
            return lambda_func(res)

        return wrapper

    return decorator_func


@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) -> int:
    return num


if __name__ == '__main__':
    res1 = return_user_id(42)
    print(f"res1: {res1}")
    assert res1 == 43
