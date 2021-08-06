# https://leetcode.com/problems/contains-duplicate/

def contains_duplicate(nums: list) -> bool:
    """ With extra memory
    Return True if any value appears at least twice in the array,
    and return False if every element is distinct.

    nums: list[int]
    rtype: bool
    """
    nums_set = set()

    for num in nums:
        if num in nums_set:
            return True
        nums_set.add(num)

    return False


def contains_duplicate(nums: list) -> bool:
    """Without extra memory
    Return True if any value appears at least twice in the array,
    and return False if every element is distinct.

    nums: list[int]
    rtype: bool
    """
    nums.sort()

    for i in range(len(nums) - 1):
        if nums[i+1] == nums[i]:
            return True

    return False
