# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq


def find_kth_largest(nums: list[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]


def find_kth_largest(nums: list[int], k: int) -> int:
    return sorted(nums, reverse=True)[k - 1]


def find_kth_largest(nums: list[int], k: int) -> int:
    heap = []
    for num in nums:
        if len(heap) == k:
            heapq.heappushpop(heap, num)
        else:
            heapq.heappush(heap, num)
