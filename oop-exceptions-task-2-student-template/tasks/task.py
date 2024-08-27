from typing import Union


def get_error_msg(msg: str):
    return f"Error code: {msg}"


def divide(str_with_ints: str) -> Union[float, str]:
    dividend, divisor = str_with_ints.split()

    if not dividend.isnumeric():
        return get_error_msg(f"invalid literal for int() with base 10: '{dividend}'")

    if not divisor.isnumeric():
        return get_error_msg(f"invalid literal for int() with base 10: '{divisor}'")

    if int(divisor) == 0:
        return get_error_msg("division by zero")

    return int(dividend) / int(divisor)


if __name__ == '__main__':
    res = divide("4 2")
    print(f'res={res}')
    assert res == 2.0

    res = divide("4 0")
    print(f'res={res}')
    assert res == "Error code: division by zero"

    res = divide("* 1")
    print(f'res={res}')
    assert "Error code: invalid literal for int() with base 10: '*'"

    res = divide("$ 1")
    print(f'res={res}')
    assert "Error code: invalid literal for int() with base 10: '$'"

    res = divide("% &")
    print(f'res={res}')
    assert "Error code: invalid literal for int() with base 10: '%'"
