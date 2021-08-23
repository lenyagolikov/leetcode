# https://leetcode.com/problems/merge-two-binary-trees/

class TreeNode:
    def __init__(self, value=0, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def merge_trees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        """Return the merged tree"""
        if root1 is None:
            return root2

        if root2 is None:
            return root1

        root1.value += root2.value

        root1.left = self.merge_trees(root1.left, root2.left)
        root1.right = self.merge_trees(root1.right, root2.right)

        return root1
