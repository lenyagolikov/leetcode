# https://leetcode.com/problems/sort-colors/


def sort_colors(nums: list[int]) -> None:
    """
    Time Complexity: O(n) - 1 pass
    Space Complexity: O(1)
    """
    red = 0
    blue = len(nums) - 1

    i = 0
    while i <= blue:
        if nums[i] == 0:
            nums[i], nums[red] = nums[red], nums[i]
            red += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[blue] = nums[blue], nums[i]
            blue -= 1
        else:
            i += 1


def sort_colors(nums: list[int]) -> None:
    """
    Time Complexity: O(n) - 2 passes
    Space Complexity: O(1)
    """
    colors = [0] * 3

    for num in nums:
        colors[num] += 1

    for i in range(len(nums)):
        if colors[0]:
            nums[i] = 0
            colors[0] -= 1
        elif colors[1]:
            nums[i] = 1
            colors[1] -= 1
        else:
            nums[i] = 2
