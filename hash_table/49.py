# https://leetcode.com/problems/group-anagrams/


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    result = []
    anagrams = {}

    for s in strs:
        sorted_s = "".join(sorted(s))
        anagrams.setdefault(sorted_s, []).append(s)

    for anagram in anagrams.values():
        result.append(anagram)

    return result
