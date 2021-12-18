# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/


def replace_element(nums: list[int]) -> list[int]:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    >>> replace_element([17, 18, 5, 4, 6, 1])
    [18, 6, 6, 6, 1, -1]
    >>> replace_element([400])
    [-1]
    """
    last_max = nums[-1]
    nums[-1] = -1

    for i in range(len(nums) - 2, -1, -1):
        current = nums[i]
        nums[i] = last_max
        last_max = max(last_max, current)

    return nums
