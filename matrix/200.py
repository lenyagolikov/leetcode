# https://leetcode.com/problems/number-of-islands/


# Закомментированный код - включение диагоналей
def num_islands(grid: list[list[str]]) -> int:
    n = len(grid)
    m = len(grid[0])
    result = 0
    stack = []

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1":
                stack.append((i, j))
            while stack:
                i, j = stack[-1]
                grid[i][j] = "0"

                if j + 1 < m and grid[i][j + 1] == "1":
                    stack.append((i, j + 1))
                elif j - 1 >= 0 and grid[i][j - 1] == "1":
                    stack.append((i, j - 1))
                elif i + 1 < n and grid[i + 1][j] == "1":
                    stack.append((i + 1, j))
                elif i - 1 >= 0 and grid[i - 1][j] == "1":
                    stack.append((i - 1, j))
                # elif i - 1 >= 0 and j - 1 >= 0 and grid[i - 1][j - 1] == "1":
                #     stack.append((i - 1, j - 1))
                # elif i - 1 >= 0 and j + 1 < m and grid[i - 1][j + 1] == "1":
                #     stack.append((i - 1, j + 1))
                # elif i + 1 < n and j - 1 >= 0 and grid[i + 1][j - 1] == "1":
                #     stack.append((i + 1, j - 1))
                # elif i + 1 < n and j + 1 < m and grid[i + 1][j + 1] == "1":
                #     stack.append((i + 1, j + 1))
                else:
                    stack.pop()
                    if not stack:
                        result += 1

    return result
