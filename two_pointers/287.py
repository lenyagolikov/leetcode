# https://leetcode.com/problems/find-the-duplicate-number/

def find_duplicate(nums: list[int]) -> int:
    """
    Return number, which repeated in array
    Time complexity: O(n)
    Extra memory space: O(1)
    """
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    slow = nums[0]

    while fast != slow:
        slow = nums[slow]
        fast = nums[fast]

    return slow
