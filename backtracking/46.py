# https://leetcode.com/problems/permutations/


def permute(nums: list[int]) -> list[list[int]]:
    result = []

    def permutations(current):
        if current == len(nums):
            result.append(nums[:])
            return

        for i in range(current, len(nums)):
            nums[i], nums[current] = nums[current], nums[i]
            permutations(current + 1)
            nums[i], nums[current] = nums[current], nums[i]

    permutations(0)

    return result
