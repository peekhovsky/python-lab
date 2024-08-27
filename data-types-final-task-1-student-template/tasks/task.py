from typing import Any, Dict, List, Set


def check(dictionaries: List[Dict[Any, Any]]) -> Set[Any]:
    values = []
    for dictionary in dictionaries:
        values.extend(dictionary.values())

    return set(values)


if __name__ == '__main__':
    input_dictionaries = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
                          {"VIII": "S007"}]

    res = check(input_dictionaries)
    print(res)
    assert res == {'S005', 'S002', 'S007', 'S001', 'S009'}
