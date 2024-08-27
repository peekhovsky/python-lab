from typing import Dict


def combine_dicts(*args: Dict[str, int]) -> Dict[str, int]:
    result_dict = {}

    for dict_item in args:
        for key, value in dict_item.items():
            acc = result_dict.get(key) if key in result_dict else 0
            result_dict.update({key: acc + value})

    return result_dict


if __name__ == '__main__':
    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100}

    res1 = combine_dicts(dict_1, dict_2)
    print(res1)
    assert res1 == {'a': 300, 'b': 200, 'c': 300}

    res2 = combine_dicts(dict_1, dict_2, dict_3)
    print(res2)
    assert res2 == {'a': 600, 'b': 200, 'c': 300, 'd': 100}
