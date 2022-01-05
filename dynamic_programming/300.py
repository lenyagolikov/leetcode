# https://leetcode.com/problems/longest-increasing-subsequence/


def gis(nums: list[int]) -> int:
    f = [0] * len(nums)

    for i in range(len(nums)):
        m = 0
        for j in range(i):
            if nums[j] < nums[i] and f[j] > m:
                m = f[j]
        f[i] = m + 1
    return max(f)
