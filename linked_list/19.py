# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove n-th node from the end of the linked list and return its head
        Time Complexity: O(n) - two passes
        Space Complexity: O(1)
        """
        count = 0
        current = head

        while current:
            count += 1
            current = current.next

        barrier = ListNode(0, head)
        current = barrier

        for i in range(count + 1):
            if i == count - n:
                current.next = current.next.next
                return barrier.next
            current = current.next


class Solution:
    def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove n-th node from the end of the linked list and return its head
        Time Complexity: O(n) - one pass
        Space Complexity: O(1)
        """
        barrier = ListNode(0, head)
        current = front = barrier

        while n > 0:
            front = front.next
            n -= 1

        while front.next is not None:
            front = front.next
            current = current.next

        current.next = current.next.next

        return barrier.next
