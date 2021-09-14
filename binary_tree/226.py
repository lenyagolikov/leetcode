# https://leetcode.com/problems/invert-binary-tree/

class TreeNode:
    def __init__(self, value=0, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def invert_tree(self, root: TreeNode) -> TreeNode:
        """Return invert binary tree"""
        if root is None:
            return None

        root.left, root.right = self.invert_tree(root.right), self.invert_tree(root.left)

        return root
