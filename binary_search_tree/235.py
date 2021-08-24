# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

class TreeNode:
    def __init__(self, value=0, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """Return LCA of two given nodes in binary search tree"""
        node = root

        while node:
            if p.value > node.value and q.value > node.value:
                node = node.right
            elif p.value < node.value and q.value < node.value:
                node = node.left
            else:
                return node
