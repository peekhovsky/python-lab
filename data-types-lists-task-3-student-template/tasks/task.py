from typing import List


def multiply(nums: List[int], skip_index: int) -> int:
    res_num = 1
    for i in range(0, len(nums)):
        if i != skip_index:
            res_num *= nums[i]

    return res_num


def foo(nums: List[int]) -> List[int]:
    return [multiply(nums, i) for i in range(0, len(nums))]


if __name__ == '__main__':
    res = foo([1, 2, 3, 4, 5])
    print(res)
    assert res == [120, 60, 40, 30, 24]

    res = foo([3, 2, 1])
    print(res)
    assert res == [2, 3, 6]
