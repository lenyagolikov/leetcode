# https://leetcode.com/problems/spiral-matrix/

def spiral_matrix(matrix: list[list[int]]) -> list[int]:
    """
    Return all elements of the matrix in spiral order
    Time Complexity: O(n*m)
    """
    result = []

    top = 0
    bottom = len(matrix) - 1

    left = 0
    right = len(matrix[0]) - 1

    # 0 - left to right, 1 - top to bot, 2 - right to left, 3 - bot to top
    direction = 0

    while top <= bottom and left <= right:
        if direction == 0:
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1
            direction = 1

        if direction == 1:
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            direction = 2

        if direction == 2:
            for j in range(right, left - 1, - 1):
                result.append(matrix[bottom][j])
            bottom -= 1
            direction = 3

        if direction == 3:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
            direction = 0

    return result
