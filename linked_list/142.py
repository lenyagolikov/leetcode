# https://leetcode.com/problems/linked-list-cycle-ii/

from typing import Optional


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def detect_cycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Return the node where the cycle begins, if not cycle return None

        Time Complexity: O(n)
        Memory: O(1)
        """
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                slow = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow
