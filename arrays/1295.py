# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/


def find_numbers(nums: list[int]) -> int:
    """Return the number of numbers with an even number of digits in the array
    >>> find_numbers([12, 345, 2, 6, 7896])
    2
    >>> find_numbers([555, 901, 482, 1771])
    1
    >>> find_numbers([4])
    0
    >>> find_numbers([24, 4843])
    2
    """
    result = 0

    for num in nums:
        current = 0
        while num > 0:
            num = num // 10
            current += 1
        if current % 2 == 0:
            result += 1

    return result


def find_numbers(nums: list[int]) -> int:
    """Return the number of numbers with an even number of digits in the array
    >>> find_numbers([12, 345, 2, 6, 7896])
    2
    >>> find_numbers([555, 901, 482, 1771])
    1
    >>> find_numbers([4])
    0
    >>> find_numbers([24, 4843])
    2
    """
    result = 0

    for num in nums:
        if len(str(num)) % 2 == 0:
            result += 1

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
