# https://leetcode.com/problems/find-all-duplicates-in-an-array/

def find_duplicates(nums: list[int]) -> list[int]:
    """
    Return an array of all the integers that appears twice in nums
    Time complexity: O(n)
    Extra memory space: 0(1)
    """
    result = []
    for num in nums:
        if nums[abs(num) - 1] < 0:
            result.append(abs(num))
        nums[abs(num) - 1] *= -1
    return result
