# https://leetcode.com/problems/maximum-subarray/

def max_subarray(nums: list) -> int:
    """Return maximum sum of subarray
    speed: O(n)
    memory: 0(1)

    nums: list[int]
    rtype: int
    """
    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        num = nums[i]

        if num > current_sum + num:
            current_sum = num
        else:
            current_sum += num
        
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum
