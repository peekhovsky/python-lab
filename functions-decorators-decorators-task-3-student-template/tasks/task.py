from functools import wraps


def validate(decorated_func):
    @wraps(decorated_func)
    def wrapper(*args):
        if any(arg < 0 or arg > 256 for arg in args):
            return "Function call is not valid!"

        return decorated_func(*args)

    return wrapper


@validate
def set_pixel(x: int, y: int, z: int) -> str:
    return "Pixel created!"


if __name__ == '__main__':
    res1 = set_pixel(10, 20, 30)
    print(f"res1: {res1}")
    assert res1 == 'Pixel created!'
    res2 = set_pixel(-10, 20, 30)
    print(f"res2: {res2}")
    assert res2 == 'Function call is not valid!'
