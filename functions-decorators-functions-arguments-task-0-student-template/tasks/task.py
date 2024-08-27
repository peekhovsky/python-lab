from typing import Dict


def generate_squares(num: int) -> Dict[int, int]:
    dictionary = {}
    for i in range(1, num + 1):
        dictionary.update({i: i ** 2})

    return dictionary


if __name__ == '__main__':
    res = generate_squares(5)
    print(res)
    assert res == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
