# https://leetcode.com/problems/duplicate-zeros/


def duplicate_zeros(nums: list[int]) -> list[int]:
    """
    Duplicate each occurrence of zero, shifting the remaing elemets to the right
    Array must be modified in-place, length is fixed

    Time Complexity: O(n^2)
    Space Complexity: O(1)

    >>> duplicate_zeros([1,0,2,3,0,4,5,0])
    [1,0,0,2,3,0,0,4]
    >>> duplicate_zeros([1, 2, 3])
    [1,2,3]
    >>> duplicate_zeros([0, 1])
    [0, 0]
    >>> duplicate_zeros([1, 1])
    [1, 1]
    >>> duplicate_zeros([0])
    [0]
    """
    i = 0

    while i < len(nums):
        if nums[i] == 0:
            nums.insert(i, 0)
            nums.pop()
            i += 1
        i += 1

    return nums


def duplicate_zeros(nums: list[int]) -> list[int]:
    """
    Duplicate each occurrence of zero, shifting the remaing elemets to the right
    Array must be modified in-place, length is fixed

    Time Complexity: O(n^2)
    Space Complexity: O(1)

    >>> duplicate_zeros([1,0,2,3,0,4,5,0])
    [1,0,0,2,3,0,0,4]
    >>> duplicate_zeros([1, 2, 3])
    [1,2,3]
    >>> duplicate_zeros([0, 1])
    [0, 0]
    >>> duplicate_zeros([1, 1])
    [1, 1]
    >>> duplicate_zeros([0])
    [0]
    """
    length = len(nums)
    i = 0

    while i < length - 1:
        if nums[i] == 0:
            for j in range(length - 2, i - 1, -1):
                nums[j + 1] = nums[j]
            i += 1
        i += 1

    return nums
