# https://leetcode.com/problems/counting-bits/

def count_bits(n: int) -> list:
    """
    Return an array ans of length n + 1 such that for each i (0 <= i <= n),
    ans[i] is the number of 1's in the binary representation of i.

    speed: O(n)
    memory: O(n)

    n: int
    rtype: list[int]
    """
    ans = [0] * (n + 1)

    for i in range(1, n + 1):
        ans[i] = ans[i//2] + i % 2

    return ans
