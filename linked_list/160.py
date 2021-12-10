# https://leetcode.com/problems/intersection-of-two-linked-lists/

from typing import Optional


class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


class Solution:
    def get_intersection_node(self, head_first: ListNode, head_second: ListNode) -> Optional[ListNode]:
        """
        Return the node at which the two lists intersect. If the two linked lists
        have no intersection, return None
        Time Complexity: O(n + m)
        Space Complexity: O(n + m)
        """
        nodes = set()

        first = head_first
        second = head_second

        while first:
            nodes.add(first)
            first = first.next

        while second:
            if second in nodes:
                return second
            second = second.next


class Solution:
    def get_intersection_node(self, head_first: ListNode, head_second: ListNode) -> Optional[ListNode]:
        """
        Return the node at which the two lists intersect. If the two linked lists
        have no intersection, return None
        Time Complexity: O(n + m)
        Space Complexity: O(1)
        """
        len_first = 0
        len_second = 0

        first = head_first
        second = head_second

        while first:
            len_first += 1
            first = first.next

        while second:
            len_second += 1
            second = second.next

        first = head_first
        second = head_second

        if len_first >= len_second:
            diff = len_first - len_second
            for _ in range(diff):
                first = first.next
        else:
            diff = len_second - len_first
            for _ in range(diff):
                second = second.next

        while first:
            if first == second:
                return first
            first = first.next
            second = second.next
