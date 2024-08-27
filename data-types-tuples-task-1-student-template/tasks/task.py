from typing import Tuple


def get_tuple(num: int) -> Tuple[int]:
    str_num = [int(num) for num in str(num)]
    return (*str_num,)


if __name__ == '__main__':
    res = get_tuple(87178291199)
    print(res)
    assert res == (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
