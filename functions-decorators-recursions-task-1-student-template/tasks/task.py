from typing import List, Tuple, Union
from functools import reduce


def summarize(*items):
    return reduce(lambda x, y: x + (y if isinstance(y, int) else summarize(*y)), items, 0)  # 15


def seq_sum(sequence: Union[List, Tuple]) -> int:
    return summarize(*sequence)


if __name__ == '__main__':
    input_sequence = [1, 2, 3, [4, 5, (6, 7)]]
    res1 = seq_sum(input_sequence)
    print(res1)
    assert res1 == 28
