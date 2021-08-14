# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: list, target: int) -> int:
        """Return index of target, if target exists. Otherwise, return -1"""
        length = len(nums)

        left = -1
        right = length

        while right - left > 1:
            middle = (left + right) // 2

            if target <= nums[middle]:
                right = middle
            else:
                left = middle

        return right if right < length and nums[right] == target else -1
