from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values

    def __add__(self, value):
        return [f'{v} {value}' for v in self.values]


if __name__ == '__main__':
    res = Counter([1, 2, 3]) + "mississippi"
    print(f'res={res}')
    assert res == ["1 mississippi", "2 mississippi", "3 mississippi"]
