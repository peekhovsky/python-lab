from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_value(number: int):
    fizzbuzz = ('Fizz' if number % 3 == 0 else '') + ('Buzz' if number % 5 == 0 else '')
    return fizzbuzz or number


def get_fizzbuzz_list(n: int) -> ListType:
    return [get_fizzbuzz_value(i) for i in range(1, n + 1)]


if __name__ == '__main__':
    res = get_fizzbuzz_list(10)
    assert res == [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz']

    res = get_fizzbuzz_list(16)
    assert res == [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16]
