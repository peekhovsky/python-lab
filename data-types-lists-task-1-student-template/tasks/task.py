from typing import List, Tuple


def sort_unique_elements(str_list: Tuple) -> List[str]:
    res_list = []

    for word in str_list:
        if res_list.count(word) == 0:
            res_list.append(word)

    res_list.sort()
    return res_list


if __name__ == '__main__':
    words = tuple(input("Input words: ").split())
    result = sort_unique_elements(words)
    print(result)

    assert sort_unique_elements(('red', 'white', 'black', 'red', 'green', 'black')) == ['black', 'green', 'red', 'white']
