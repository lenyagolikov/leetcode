# https://leetcode.com/problems/check-if-n-and-its-double-exist/


def check_if_exist(nums: list[int]) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    >>> check_if_exist([10, 2, 5, 3])
    True
    >>> check_if_exist([7, 1, 14, 1])
    True
    >>> check_if_exist([3, 1, 7, 11])
    False
    """
    s = set()

    for num in nums:
        if num * 2 in s or num / 2 in s:
            return True
        s.add(num)

    return False


def check_if_exist(nums: list[int]) -> bool:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    >>> check_if_exist([10, 2, 5, 3])
    True
    >>> check_if_exist([7, 1, 14, 1])
    True
    >>> check_if_exist([3, 1, 7, 11])
    False
    """
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] / 2 == nums[j]:
                return True
    return False
