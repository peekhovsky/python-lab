from typing import Any, Tuple, List


def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    return [(lst[i], lst[i + 1]) for i in range(0, len(lst) - 1)]


if __name__ == '__main__':
    res = get_pairs([1, 2, 3, 8, 9])
    print(res)
    assert res == [(1, 2), (2, 3), (3, 8), (8, 9)]

    res = get_pairs(['need', 'to', 'sleep', 'more'])
    print(res)
    assert res == [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]

    res = get_pairs(['need'])
    print(res)
    assert res == []
