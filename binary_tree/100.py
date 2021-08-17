# https://leetcode.com/problems/same-tree

class TreeNode:
    def __init__(self, value=0, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def same_tree(self, q: TreeNode, p: TreeNode) -> bool:
        """Return True if q and p are the same. Otherwise, return False"""
        queue = [q, p]

        while queue:
            q = queue.pop(0)
            p = queue.pop(0)

            if q is None and p is None:
                continue

            if q is None or p is None:
                return False

            if q.value != p.value:
                return False

            queue.append(q.left)
            queue.append(p.left)
            queue.append(q.right)
            queue.append(p.right)

        return True
