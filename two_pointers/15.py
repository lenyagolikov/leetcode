# https://leetcode.com/problems/3sum/


def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Time Complexity: O(n^2)
    Space Compleity: O(1)
    """
    n = len(nums)
    triplets = []

    nums.sort()

    for i in range(n - 2):
        if i == 0 or nums[i] != nums[i - 1]:
            left = i + 1
            right = n - 1

            while left < right:
                sum3 = nums[i] + nums[left] + nums[right]
                if sum3 == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum3 > 0:
                    right -= 1
                else:
                    left += 1

    return triplets
