# https://leetcode.com/problems/majority-element/

def majority_element(nums: list[int]) -> int:
    """
    Return the majority element that appears more than n//2 times
    time complexity: O(nlogn)
    extra memory space: O(1)
    """

    nums.sort()
    return nums[len(nums) // 2]


def majority_element(nums: list[int]) -> int:
    """
    Return the majority element that appears more than n//2 times
    time complexity: O(n)
    extra memory space: 0(1)
    """
    result = None
    vote = 0

    for num in nums:
        if vote == 0:
            result = num
        if num == result:
            vote += 1
        else:
            vote -= 1

