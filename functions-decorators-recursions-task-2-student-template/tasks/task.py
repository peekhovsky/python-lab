from typing import Any, List


def flat(seq: List[Any]) -> List[Any]:
    seq_len = len(seq)

    if seq_len == 0:
        return []

    item1 = seq[0]

    if isinstance(item1, int):
        return [item1, *flat(seq[1:])]
    else:
        return [*flat(item1), *flat(seq[1:])]


def linear_seq(sequence: List[Any]) -> List[Any]:
    return flat(sequence)


if __name__ == '__main__':
    input_sequence = [1, 2, 3, [4, 5, (6, 7)]]
    res1 = linear_seq(input_sequence)
    print(res1)
    assert res1 == [1, 2, 3, 4, 5, 6, 7]
