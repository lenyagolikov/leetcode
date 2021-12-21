# https://leetcode.com/discuss/interview-question/341247/facebook-leftmost-column-index-of-1
# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/ - only premium leetcode


def find_leftmost_one(matrix: list[list[int]]) -> int:
    j = len(matrix) - 1

    for i in range(len(matrix)):
        while j >= 0 and matrix[i][j]:
            j -= 1

    return j + 1
