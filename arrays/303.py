# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:
    """Calculate the sum of the elements of nums between indices left and right inclusive"""

    def __init__(self, nums: list) -> None:
        self.sums = [0]

        for num in nums:
            current_sum = self.sums[-1] + num
            self.sums.append(current_sum)

    def sum_range(self, left: int, right: int) -> int:
        return self.sums[right + 1] - self.sums[left]
