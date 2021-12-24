# https://leetcode.com/problems/increasing-triplet-subsequence/


def increasing_triplet(nums: list[int]) -> bool:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    result = [nums[0]]
    visited = set()

    for i in range(1, len(nums)):
        if len(result) == 1 and nums[i] not in visited:
            if nums[i] <= result[0]:
                result[0] = nums[i]
            else:
                result.append(nums[i])
        if len(result) == 2:
            ptr = i
            while ptr < len(nums):
                if nums[ptr] > result[-1]:
                    return True
                ptr += 1
            visited.add(result.pop())

    return False


def increasing_triplet(nums: list[int]) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    first = float("inf")
    second = float("inf")

    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True

    return False
