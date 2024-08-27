from typing import Union

NumType = Union[int, float]


def some_expression_with_rounding(a: NumType, b: NumType) -> NumType:
    result = (12 * a + 25 * b) / (1 + a ** (2 ** b))
    return round(result, 2)


if __name__ == '__main__':
    assert some_expression_with_rounding(1, 2) == 31.0
    assert some_expression_with_rounding(11.345, -2.3) == 29.82
