# https://leetcode.com/problems/merge-sorted-array/


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    """
    Merge two sorted array in-place

    Time Complexity: O(n)
    Space Complexity: O(1)

    >>> merge([1,2,3,0,0,0], 3, [2,5,6], 3)
    [1, 2, 2, 3, 5, 6]
    >>> merge([1], 1, [], 0)
    [1]
    >>> merge([0], 0, [1], 1)
    [1]
    """
    index1, index2 = m - 1, n - 1

    for i in range(len(nums1) - 1, -1, -1):
        val1 = nums1[index1] if index1 >= 0 else float("-inf")
        val2 = nums2[index2] if index2 >= 0 else float("-inf")

        if val1 >= val2:
            nums1[i] = val1
            index1 -= 1
        else:
            nums1[i] = val2
            index2 -= 1


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    """
    Merge two sorted array in-place

    Time Complexity: O(n^2)
    Space Complexity: O(1)

    >>> merge([1,2,3,0,0,0], 3, [2,5,6], 3)
    [1, 2, 2, 3, 5, 6]
    >>> merge([1], 1, [], 0)
    [1]
    >>> merge([0], 0, [1], 1)
    [1]
    """
    i = 0

    for num in nums2:
        while m != 0 and nums1[i] <= num:
            i += 1
            m -= 1
        nums1.insert(i, num)
        nums1.pop()
        i += 1

    return nums1
