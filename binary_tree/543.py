# https://leetcode.com/problems/diameter-of-binary-tree/

class TreeNode:
    def __init__(self, value=0, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def diameter_of_binary_tree(self, root: TreeNode) -> int:
        """Return the length of the diameter of binary tree, diameter it is longest path between any nodes"""
        self.diameter = 0

        def longest_path(node):
            if node is None:
                return 0

            left = longest_path(node.left)
            right = longest_path(node.right)

            self.diameter = max(self.diameter, left + right)

            return max(left, right) + 1

        longest_path(root)

        return self.diameter
