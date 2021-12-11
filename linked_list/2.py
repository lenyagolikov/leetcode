# https://leetcode.com/problems/add-two-numbers/

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Additional two numbers and return the sum as a linked list
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        result = ListNode(0)
        current = result
        mind = 0

        while l1 and l2:
            add = l1.val + l2.val + mind
            mind = 1 if add > 9 else 0
            add = add % 10
            
            current.next = ListNode(add)
            current = current.next
            l1 = l1.next
            l2 = l2.next

        remainder = l1 if l1 else l2

        while remainder:
            add = remainder.val + mind
            mind = 1 if add > 9 else 0
            add = add % 10
            
            current.next = ListNode(add)
            current = current.next
            remainder = remainder.next

        if mind:
            current.next = ListNode(1)

        return result.next
