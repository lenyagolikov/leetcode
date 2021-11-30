# https://leetcode.com/problems/product-of-array-except-self/

def product_except_self(nums: list) -> list[int]:
    """
    Return array result such that result[i] is equal to the product of all
    the elements of nums except nums[i]
    Time complexity: O(N)
    Extra memory space: O(N)
    """
    n = len(nums)

    left = [1] * n
    right = [1] * n
    result = [1] * n

    for i in range(1, n):
        left[i] = nums[i - 1] * left[i - 1]

    for i in range(n - 2, -1, -1):
        right[i] = nums[i + 1] * right[i + 1]

    for i in range(n):
        result[i] = left[i] * right[i]

    return result


def product_except_self(nums: list) -> list[int]:
    """
    Return array result such that result[i] is equal to the product of all
    the elements of nums except nums[i]
    Time complexity: O(N)
    Extra memory space: O(1)
    """
    n = len(nums)

    result = [1] * n
    right = 1

    for i in range(1, n):
        result[i] = nums[i - 1] * result[i - 1]

    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= nums[i]

    return result
