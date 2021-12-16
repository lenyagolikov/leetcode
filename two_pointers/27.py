# https://leetcode.com/problems/remove-element/

import doctest


def remove_element(nums: list[int], val: int) -> int:
    """
    Time Complexity: O(n) - 1 pass
    Space Complexity: O(1)
    >>> remove_element([3, 2, 2, 3], 3)
    2
    >>> remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2)
    5
    >>> remove_element([2, 3, 3], 3)
    1
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        if nums[left] == val:
            nums[left], nums[right] = nums[right], nums[left]
            nums[right] = "_"
            right -= 1
        else:
            left += 1

    return right + 1


doctest.testmod()
