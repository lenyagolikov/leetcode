# https://leetcode.com/problems/letter-case-permutation/

def letter_case_permutation(s: str) -> list[str]:
    """
    Return list of all possible strings we could create with transform
    every letter to lowercase or uppercase
    Time Complexity: O(2^k * n), k - number of letters, n - length of s
    """
    result = []
    traverse([], s, 0, result)
    return result


def traverse(current: str, s: str, i: int, result: list) -> None:
    if len(current) == len(s):
        result.append(''.join(current))
        return

    traverse(current + [s[i]], s, i + 1, result)

    if s[i].isalpha():
        traverse(current + [s[i].swapcase()], s, i + 1, result)
