# https://leetcode.com/problems/longest-substring-without-repeating-characters/


def length_of_longest_substring(string: str) -> int:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    result = 0
    substring = ""

    for char in string:
        if char in substring:
            result = max(result, len(substring))
            substring = substring[substring.find(char) + 1 :]
        substring += char

    return max(result, len(substring))


def length_of_longest_substring(string: str) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    result = 0
    ptr = 0
    prev_values = set()

    for char in string:
        if char not in prev_values:
            prev_values.add(char)
            result = max(len(prev_values), result)
        else:
            while string[ptr] != char:
                prev_values.remove(string[ptr])
                ptr += 1
            ptr += 1

    return result
