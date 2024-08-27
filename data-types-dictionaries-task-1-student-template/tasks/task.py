from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    char_dict = {}

    for char in s.lower():
        if char in char_dict and char_dict[char]:
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1

    return char_dict


if __name__ == '__main__':
    res = get_dict('Oh, it is python')
    print(res)
    assert res == {" ": 3, ",": 1, "h": 2, "i": 2, "n": 1, "o": 2, "p": 1, "s": 1, "t": 2, "y": 1}
