# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

def missing_numbers(nums: list) -> list:
    """Return an array of all the integers in the range [1, n] that do not appear in nums

    nums: list[int]
    rtype: list[int]
    """
    n = len(nums)
    nums = set(nums)
    result = []

    for num in range(1, n + 1):
        if num not in nums:
            result.append(num)

    return result


def missing_numbers(nums: list) -> list:
    """Return an array of all the integers in the range [1, n] that do not appear in nums
    Without extra memory (cyclic sort)

    nums: list[int]
    rtype: list[int]
    """
    i = 0
    while i < len(nums):
        pos = nums[i] - 1
        if nums[i] != nums[pos]:
            nums[i], nums[pos] = nums[pos], nums[i]
        else:
            i += 1

    result = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            result.append(i + 1)

    return result
