# https://leetcode.com/problems/height-checker/


def height_checker(heights: list[int]) -> int:
    """
    Time Complexity: O(nlogn)
    Space Complexity: O(n)
    >>> height_checker([1, 1, 4, 2, 1, 3])
    3
    >>> height_checker([5, 1, 2, 3, 4])
    3
    >>> height_checker([1, 2, 3, 4, 5])
    0
    """
    result = 0
    another = sorted(heights)

    for i in range(len(heights)):
        if another[i] != heights[i]:
            result += 1

    return result


def height_checker(heights: list[int]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    >>> height_checker([1, 1, 4, 2, 1, 3])
    3
    >>> height_checker([5, 1, 2, 3, 4])
    3
    >>> height_checker([1, 2, 3, 4, 5])
    0
    """
    result = 0
    hashmap = {value: 0 for value in range(1, 101)}
    another = []

    for height in heights:
        hashmap[height] += 1

    for height, total in hashmap.items():
        for _ in range(total):
            another.append(height)

    for i in range(len(heights)):
        if another[i] != heights[i]:
            result += 1

    return result
