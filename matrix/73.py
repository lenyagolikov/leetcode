# https://leetcode.com/problems/set-matrix-zeroes/

def set_zeroes(matrix: list[list[int]]) -> None:
    """
    If an element is 0, set it's entire row and column to 0's (in-place)
    Time complexity: O(n*m)
    Extra space: O(n+m)
    """
    n = len(matrix)
    m = len(matrix[0])
    rows = set()
    cols = set()

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for i in range(n):
        for j in range(m):
            if i in rows or j in cols:
                matrix[i][j] = 0


def set_zeroes(matrix: list[list[int]]) -> None:
    """
    If an element is 0, set it's entire row and column to 0's (in-place)
    Time complexity: O(n*m)
    Extra space: O(1)
    """
    n = len(matrix)
    m = len(matrix[0])
    is_col = False

    for i in range(n):
        if matrix[i][0] == 0:
            is_col = True
        for j in range(1, m):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0

    if is_col:
        for i in range(n):
            matrix[i][0] = 0
