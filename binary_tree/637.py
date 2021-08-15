# https://leetcode.com/problems/average-of-levels-in-binary-tree/

class TreeNode:
    def __init__(self, value=0, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def average_of_levels(self, root: TreeNode) -> list:
        """Return the average value of the nodes on each level in the form of an array"""
        queue = [root]
        averages = []

        while queue:
            length = len(queue)
            level_sum = 0

            for _ in range(length):
                node = queue.pop(0)
                level_sum += node.value

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            averages.append(level_sum / length)

        return averages
