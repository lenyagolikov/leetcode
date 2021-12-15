# https://leetcode.com/problems/rotate-list/

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotate_right(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Rotate the linked list to the right by k places
        Time Complexity: O(n) - 2 passes
        Space Complexity: O(1)
        """
        if not head:
            return head

        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        k = k % length
        if k == 0:
            return head

        counter = 0
        current = head
        while current:
            if counter == length - k - 1:
                next = current.next
                result = next
                current.next = None
                while next:
                    last = next
                    next = next.next
                last.next = head
                return result
            current = current.next
            counter += 1
