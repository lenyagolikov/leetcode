# https://leetcode.com/problems/max-consecutive-ones/


def find_max_consecutive_ones(nums: list[int]) -> int:
    """Return the max number of consecutive 1 's' in the array
    >>> find_max_consecutive_ones([1,1,0,1,1,1])
    3
    >>> find_max_consecutive_ones([1,0,1,1,0,1])
    2
    >>> find_max_consecutive_ones([1, 1, 0, 1, 1, 1, 0])
    3
    >>> find_max_consecutive_ones([1])
    1
    >>> find_max_consecutive_ones([0])
    0
    """
    result = 0
    current = 0

    for num in nums:
        if num:
            current += 1
            result = max(result, current)
        else:
            current = 0

    return result


def find_max_consecutive_ones(nums: list[int]) -> int:
    """Return the max number of consecutive 1 's' in the array
    >>> find_max_consecutive_ones([1,1,0,1,1,1])
    3
    >>> find_max_consecutive_ones([1,0,1,1,0,1])
    2
    >>> find_max_consecutive_ones([1, 1, 0, 1, 1, 1, 0])
    3
    >>> find_max_consecutive_ones([1])
    1
    >>> find_max_consecutive_ones([0])
    0
    """
    result = 0
    current = 0

    for num in nums:
        if num:
            current += 1
            continue
        result = max(result, current)
        current = 0

    return max(result, current)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
