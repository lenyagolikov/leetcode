# https://leetcode.com/problems/missing-number/

def missing_number(nums: list) -> int:
    """Return the only number in the range that is missing from the array.
    speed: O(nlogn) + O(n)
    memory: 0(1)

    nums: list[int]
    rtype: int
    """
    nums.sort()

    for i, num in enumerate(nums):
        if i != num:
            return num - 1
    return i + 1


def missing_number(nums: list) -> int:
    """Return the only number in the range that is missing from the array.
    speed: O(n)
    memory: 0(1)

    nums: list[int]
    rtype: int
    """
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)
