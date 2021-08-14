# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def next_greatest_letter(self, letters: list, target: str) -> str:
        """Return the smallest character in the array that is larger than target

        speed: O(n)
        """
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]


class Solution:
    def next_greatest_letter(self, letters: list, target: str) -> str:
        """Return the smallest character in the array that is larger than target

        speed: O(logn)
        """
        length = len(letters)
        left = -1
        right = length

        while right - left > 1:
            middle = (left + right) // 2

            if target < letters[middle]:
                right = middle
            else:
                left = middle

        return letters[right % length]
