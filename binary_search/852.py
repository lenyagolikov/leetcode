# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peak_index_in_mountain_array(self, arr: list) -> int:
        """Return index of maximum element (in mountain array) for O(logn)"""
        left = -1
        right = len(arr)

        while right - left > 1:
            middle = (left + right) // 2

            if arr[middle] > arr[middle + 1]:
                right = middle
            else:
                left = middle

        return right


class Solution:
    def peak_index_in_mountain_array(self, arr: list) -> int:
        """Return index of maximum element (in mountain array) for O(logn)"""
        left = 0
        right = len(arr) - 1

        while left <= right:
            middle = (left + right) // 2

            if arr[middle] > arr[middle + 1]:
                right = middle - 1
            else:
                left = middle + 1

        return left
