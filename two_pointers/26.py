# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

import doctest


def remove_duplicates(nums: list[int]) -> int:
    """
    Time Complexity: O(n) - 1 pass
    Space Complexity: O(1)
    >>> remove_duplicates([1, 1, 2])
    2
    >>> remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    5
    """
    write_pointer = 1 if nums else 0

    for read_pointer in range(1, len(nums)):
        if nums[read_pointer] != nums[read_pointer - 1]:
            nums[write_pointer] = nums[read_pointer]
            write_pointer += 1

    return write_pointer


def remove_duplicates(nums: list[int]) -> int:
    """
    Time Complexity: O(n) - 2 passes
    Space Complexity: O(1)
    >>> remove_duplicates([1, 1, 2])
    2
    >>> remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    5
    """
    result = len(nums)
    prev = None

    for i in range(len(nums)):
        if nums[i] == prev:
            result -= 1
            nums[i] = "_"
        else:
            prev = nums[i]

    n = len(nums) - 1
    left = 0
    right = 1

    while right < n:
        while left < n and nums[left] != "_":
            left += 1
        while right < n and (left > right or nums[right] == "_"):
            right += 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]

    return result


doctest.testmod()
