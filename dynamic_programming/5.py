# https://leetcode.com/problems/longest-palindromic-substring/


def longest_palindrome(s: str) -> str:
    """
    Time Complexity: O(n^2) - long decision
    Space Complexity: O(1)
    """
    for window in range(len(s), 1, -1):
        for i in range(len(s) - window + 1):
            current_window = s[i : i + window]
            if current_window == current_window[::-1]:
                return current_window
    return s[0]


def longest_palindrome(s: str) -> str:
    """
    Time Complexity: O(n^2) - faster than sliding window
    Space Complexity: O(1)
    """

    def helper(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    result = ""

    for i in range(len(s)):
        odd = helper(i, i)
        even = helper(i, i + 1)
        result = max(odd, even, result, key=lambda x: len(x))

    return result


def longest_palindrome(s: str) -> str:
    """
    Time Complexity: O(n) - very fast solution
    Space Complexity: O(1)
    """
    if s == s[::-1]:
        return s

    longest, current = 1, 1

    for i in range(1, len(s)):
        odd_left, even_left = i - current - 1, i - current
        odd, even = s[odd_left : i + 1], s[even_left : i + 1]
        if odd_left >= 0 and odd == odd[::-1]:
            longest = odd_left
            current += 2
        elif even_left >= 0 and even == even[::-1]:
            longest = even_left
            current += 1

    return s[longest : longest + current]
