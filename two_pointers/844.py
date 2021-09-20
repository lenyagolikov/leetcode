# https://leetcode.com/problems/backspace-string-compare/

# first way of solving, stack - O(n) time, O(n*k) - extra space
def backspace_compare(s: str, t: str) -> bool:
    """Return True if two strings are equal when both are typed into empty editors. # - backspace"""
    len_s = len(s)
    len_t = len(t)
    max_length = max(len_s, len_t)

    sstack = []
    tstack = []

    for i in range(max_length):
        if i < len_s and s[i] == '#':
            if sstack:
                sstack.pop()
        elif i < len_s:
            sstack.append(s[i])

        if i < len_t and t[i] == '#':
            if tstack:
                tstack.pop()
        elif i < len_t:
            tstack.append(t[i])

    return sstack == tstack


# second way to solving, two pointers - O(n) time, O(1) - extra space
def get_current_index(s: str, i: int) -> int:
    """Return index of string which not equal #"""
    to_skip = 0

    while i >= 0:
        if s[i] == '#':
            to_skip += 1
        elif to_skip > 0:
            to_skip -= 1
        else:
            break
        i -= 1

    return i


def backspace_compare(s: str, t: str) -> bool:
    """Return True if two strings are equal when both are typed into empty editors. # - backspace"""
    i = len(s) - 1
    j = len(t) - 1

    while i >= 0 or j >= 0:
        i = get_current_index(s, i)
        j = get_current_index(t, j)

        if i < 0 and j < 0:
            return True
        if i < 0 or j < 0:
            return False
        if s[i] != t[j]:
            return False

        i -= 1
        j -= 1

    return True
