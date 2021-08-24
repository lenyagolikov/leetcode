# https://leetcode.com/problems/subtree-of-another-tree/

class TreeNode:
    def __init__(self, value=0, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def is_sub_tree(self, root: TreeNode, sub_root: TreeNode) -> bool:
        """
        Return True if there is a subtree of root with the same structure and node values
        of subRoot and False otherwise.
        """
        if not root:
            return False

        if self.is_same_tree(root, sub_root):
            return True

        return self.is_sub_tree(root.left, sub_root) or self.is_sub_tree(root.right, sub_root)

    def is_same_tree(self, q: TreeNode, p: TreeNode) -> bool:
        """Return True if q is equal p"""
        if not q and not p:
            return True

        if not q or not p:
            return False

        if q.value != p.value:
            return False

        return self.is_same_tree(q.left, p.left) and self.is_same_tree(q.right, p.right)
