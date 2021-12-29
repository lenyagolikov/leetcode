# https://leetcode.com/problems/jump-game/


def can_jump(nums: list[int]) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    target = len(nums) - 1
    current = 0

    for i in range(target):
        if i + nums[i] >= target:
            return True

        current = max(nums[i], current - 1)
        if current == 0:
            return False

    return True


def can_jump(nums: list[int]) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    target = len(nums) - 1

    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= target:
            target = i

    return target == 0
