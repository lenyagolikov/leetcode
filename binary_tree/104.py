# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class TreeNode:
    def __init__(self, value=0, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def max_depth(self, root: TreeNode) -> int:
        """Return maximum depth of binary tree with while loop and stack"""
        max_depth = 0
        current_depth = 1
        stack = [root]
        visited = [root]

        if root is None:
            return max_depth

        while stack:
            node = stack[-1]

            if node.left and node.left not in visited:
                stack.append(node.left)
                visited.append(node.left)
                current_depth += 1
            elif node.right and node.right not in visited:
                stack.append(node.right)
                visited.append(node.right)
                current_depth += 1
            else:
                max_depth = max(max_depth, current_depth)
                current_depth -= 1
                stack.pop()

        return max_depth


class Solution:
    def max_depth(self, root: TreeNode) -> int:
        """Return maximum depth of binary tree with recursion"""
        if root is None:
            return 0

        left = self.max_depth(root.left)
        right = self.max_depth(root.right)

        return max(left, right) + 1
