# https://leetcode.com/problems/minimum-depth-of-binary-tree/

class TreeNode:
    def __init__(self, value=0, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def min_depth(self, root: TreeNode) -> int:
        """Return minimum depth of binary tree"""
        queue = [root]
        depth = 0

        while root and queue:
            length = len(queue)
            depth += 1

            for _ in range(length):
                node = queue.pop(0)

                if not node.left and not node.right:
                    return depth

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return depth
