# https://leetcode.com/problems/top-k-frequent-elements/

import heapq
from collections import Counter


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """
    Time Complexity: O(nlogn)
    Space Complexity: O(n)
    """
    counter = Counter(nums)
    counter = sorted(counter, key=lambda x: counter[x], reverse=True)
    return counter[:k]


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """
    Time Complexity: O(n + k)
    Space Complexity: O(n)
    """
    counter = Counter(nums)
    freq = [(-val, key) for key, val in counter.items()]
    heapq.heapify(freq)
    return [heapq.heappop(freq)[1] for _ in range(k)]
