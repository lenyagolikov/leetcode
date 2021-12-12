# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

from typing import Optional


class ListNode:
    def __init__(
        self,
        val: int,
        prev: "Optional[ListNode]",
        next: "Optional[ListNode]",
        child: "Optional[ListNode]",
    ) -> None:
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Return the head of the flatten linked list
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        stack = [head]
        prev = None

        while stack:
            current = stack.pop()
            if current:
                current.prev = prev
                stack.append(current.next)
                if prev:
                    prev.next = current
                prev = current
                if current.child:
                    current.next = current.child
                    stack.append(current.child)
                    current.child = None

        return head


class Solution:
    def flatten(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Return the head of the flatten linked list
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        result = ListNode(0)
        link_to_result = result
        stack = []
        prev = None

        while head:
            result.next = head
            result.next.prev = prev
            result = result.next
            prev = head

            if not head.child:
                head = head.next
            else:
                if head.next:
                    stack.append(head.next)
                child = head.child
                head.child = None
                head = child
            if stack and not head:
                head = stack.pop()
                head.prev = prev

        return link_to_result.next
