from typing import List


def generate_row(row_number: int, column_start: int, column_end: int):
    return [row_number * col_number for col_number in range(column_start, column_end + 1)]


def check(row_start: int, row_end: int, column_start: int, column_end: int) -> List[List[int]]:
    return [generate_row(row_number, column_start, column_end) for row_number in range(row_start, row_end + 1)]


if __name__ == '__main__':
    res = check(2, 4, 3, 7)
    print(res)
    assert res == [[6, 8, 10, 12, 14], [9, 12, 15, 18, 21], [12, 16, 20, 24, 28]]
