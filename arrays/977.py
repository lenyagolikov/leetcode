# https://leetcode.com/problems/squares-of-a-sorted-array/
import collections


def sorted_squares(nums: list) -> list:
    """Return array of the squares of each number sorted in non-decreasing order"""
    result = collections.deque()
    left = 0
    right = len(nums) - 1

    while left < right:
        if abs(nums[left]) < abs(nums[right]):
            result.appendleft(nums[right] ** 2)
            right -= 1
        else:
            result.appendleft(nums[left] ** 2)
            left += 1
    result.appendleft(nums[left] ** 2)
    return list(result)


def sorted_squares(nums: list) -> list:
    """Return array of the squares of each number sorted in non-decreasing order"""
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1

    for i in range(n - 1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            result[i] = nums[right] ** 2
            right -= 1
        else:
            result[i] = nums[left] ** 2
            left += 1

    return result
