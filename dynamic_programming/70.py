# https://leetcode.com/problems/climbing-stairs/

def climb_stairs(n: int) -> int:
    """Return number of ways to climb to the top (n)
    speed: O(n)
    memory: 0(n)

    n: int
    rtype: int
    """
    k = [0, 1, 2] + [0] * (n-2)

    for i in range(3, n + 1):
        k[i] = k[i-2] + k[i-1]

    return k[n]


def climb_stairs(n: int) -> int:
    """Return number of ways to climb to the top (n)
    speed: O(n)
    memory: 0(1)

    n: int
    rtype: int
    """
    if n == 1:
        return 1

    n1 = 1
    n2 = 2

    for _ in range(3, n + 1):
        n1, n2 = n2, n1 + n2

    return n2
