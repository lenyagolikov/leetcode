# https://leetcode.com/problems/sort-array-by-parity/

import doctest


def sort_array_by_parity(nums: list[int]) -> list[int]:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)
    >>> sort_array_by_parity([3, 1, 2, 4])
    [2, 4, 3, 1]
    >>> sort_array_by_parity([2, 1, 3, 4])
    [2, 4, 3, 1]
    >>> sort_array_by_parity([0])
    [0]
    """
    first = 0

    for second in range(len(nums)):
        if nums[second] % 2 == 0:
            nums[first], nums[second] = nums[second], nums[first]
            first += 1

    return nums


def sort_array_by_parity(nums: list[int]) -> list[int]:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)
    >>> sort_array_by_parity([3, 1, 2, 4])
    [2, 4, 3, 1]
    >>> sort_array_by_parity([2, 1, 3, 4])
    [2, 4, 3, 1]
    >>> sort_array_by_parity([0])
    [0]
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        if nums[right] % 2 == 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        else:
            right -= 1

    return nums


doctest.testmod()
