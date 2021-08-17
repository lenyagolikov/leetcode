# https://leetcode.com/problems/path-sum/

class TreeNode:
    def __init__(self, value=0, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def has_path_sum(self, root: TreeNode, target_sum: int) -> bool:
        """ Stack / visited points
        Return True if tree has a root-to-leaf path such that adding up
        all the values along the path equals target_sum.
        """
        stack = [root]
        visited = [root]
        sum = root.value if root else 0

        while stack:
            node = stack[-1]

            if node is None:
                return False

            if node.left is None and node.right is None:
                if sum == target_sum:
                    return True

            if node.left and node.left not in visited:
                stack.append(node.left)
                visited.append(node.left)
                sum += node.left.value
            elif node.right and node.right not in visited:
                stack.append(node.right)
                visited.append(node.right)
                sum += node.right.value
            else:
                sum -= node.value
                stack.pop()


class Solution:
    def has_path_sum(self, node: TreeNode, target_sum: int) -> bool:
        """ Recursion
        Return True if tree has a root-to-leaf path such that adding up
        all the values along the path equals target_sum.
        """
        if node is None:
            return False

        if node.left is None and node.right is None:
            return target_sum == 0

        return self.has_path_sum(node.left, target_sum - node.value) or \
            self.has_path_sum(node.right, target_sum - node.value)
