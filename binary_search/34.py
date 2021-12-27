# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


def search_range(nums: list[int], target: int) -> list[int]:
    """
    Time Complexity: O(n) - in worst case, average - O(logn)
    Space Complexity: O(1)
    """
    left = -1
    right = len(nums)

    while right - left > 1:
        mid = (left + right) // 2

        if nums[mid] >= target:
            right = mid
        else:
            left = mid

    if right < len(nums) and nums[right] == target:
        i = right
        while i + 1 < len(nums) and nums[i + 1] == target:
            i += 1
        return [right, i]
    return [-1, -1]


def search_range(nums: list[int], target: int) -> list[int]:
    """
    Time Complexity: O(logn) - binary search 2 times for right value and for left value
    Space Complexity: O(1)
    """
    left = -1
    right = len(nums)

    while right - left > 1:
        mid = (left + right) // 2

        if nums[mid] >= target:
            right = mid
        else:
            left = mid
    first = right

    left = -1 
    right = len(nums)

    while right - left > 1:
        mid = (left + right) // 2

        if nums[mid] > target:
            right = mid
        else:
            left = mid

    second = right - 1

    if first < len(nums) and second < len(nums) and nums[first] == target and nums[second] == target:
        return [first, second]

    return [-1, -1]
