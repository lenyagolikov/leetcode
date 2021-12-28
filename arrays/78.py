# https://leetcode.com/problems/subsets/


def subsets(nums: list[int]) -> list[list[int]]:
    result = [[]]

    for num in nums:
        result.extend([subset + [num] for subset in result])

    return result
