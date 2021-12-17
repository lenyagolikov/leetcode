# https://leetcode.com/problems/valid-mountain-array/


def valid_mountain_array(nums: list[int]) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    >>> valid_mountain_array([2, 1])
    False
    >>> valid_mountain_array([3, 5, 5])
    False
    >>> valid_mountain_array([0, 3, 2, 1])
    True
    """
    if len(nums) < 3:
        return False

    for i in range(len(nums) - 1):
        if nums[i + 1] <= nums[i]:
            break

    if i == 0:
        return False

    for j in range(i, len(nums) - 1):
        if nums[j + 1] >= nums[j]:
            return False

    return True
