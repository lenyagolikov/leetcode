# https://leetcode.com/problems/third-maximum-number/


def third_max(nums: list[int]) -> int:
    """
    Time Complexity: O(nlogn)
    Space Complexity: O(n)
    >>> third_max([3, 2, 1])
    1
    >>> third_max([1, 2])
    2
    >>> third_max([2, 2, 3, 1])
    1
    """
    nums = sorted(set(nums))

    if len(nums) >= 3:
        return nums[-3]

    return nums[-1]


def third_max(nums: list[int]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    >>> third_max([3, 2, 1])
    1
    >>> third_max([1, 2])
    2
    >>> third_max([2, 2, 3, 1])
    1
    """
    inf = float("-inf")
    max1, max2, max3 = inf, inf, inf

    for num in nums:
        if max1 < num:
            max1, max2, max3 = num, max1, max2
        elif max2 < num and num != max1:
            max2, max3 = num, max2
        elif max3 < num and num != max1 and num != max2:
            max3 = num

    return max3 if max3 != inf else max1
