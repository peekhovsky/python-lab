from typing import List


def split_by_index(s: str, raw_indexes: List[int]) -> List[str]:
    indexes = sorted(filter(lambda i: 0 <= i <= len(s), (0, *raw_indexes, len(s))))
    index_pairs = [(indexes[i - 1], indexes[i]) for i in range(1, len(indexes))]
    return [s[x:y] for x, y in index_pairs]


if __name__ == '__main__':
    res1 = split_by_index("pythoniscool,isn'tit?", [8, 6, 12, 13, 18])
    print(f"res1: {res1}")
    assert res1 == ["python", "is", "cool", ",", "isn't", "it?"]
    res2 = split_by_index("no luck", [42])
    print(f"res2: {res2}")
    assert res2 == ["no luck"]
