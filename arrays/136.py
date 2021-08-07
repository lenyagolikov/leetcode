# https://leetcode.com/problems/single-number/

def single_number(nums: list) -> int:
    """Return element which appears in the array only once

    nums: list[int]
    rtype: int
    """
    mask = 0

    for num in nums:
        mask ^= num  # XOR

    return mask
