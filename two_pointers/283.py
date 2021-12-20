# https://leetcode.com/problems/move-zeroes/

import doctest


def move_zeroes(nums: list[int]) -> list[int]:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)
    >>> move_zeroes([0, 1, 0, 3, 12])
    [1, 3, 12, 0, 0]
    >>> move_zeroes([0])
    [0]
    >>> move_zeroes([1, 2])
    [1, 2]
    >>> move_zeroes([10, 20, 0])
    [10, 20, 0]
    """
    write_pointer = 0

    for read_pointer in range(len(nums)):
        if nums[read_pointer]:
            nums[write_pointer] = nums[read_pointer]
            write_pointer += 1

    for i in range(write_pointer, len(nums)):
        nums[i] = 0

    return nums


doctest.testmod()
