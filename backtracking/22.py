# https://leetcode.com/problems/generate-parentheses/


def generate_parentheses(n: int) -> list[str]:
    result = []

    def generate(current, open, closed):
        if open + closed == 2 * n:
            result.append(current)
            return
        if open < n:
            generate(current + "(", open + 1, closed)
        if closed < open:
            generate(current + ")", open, closed + 1)

    generate("", 0, 0)

    return result
