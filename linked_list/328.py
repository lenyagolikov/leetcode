# https://leetcode.com/problems/odd-even-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def odd_even_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Transform linked list: indices of even elements go first, then odd ones
        """
        if not head:
            return

        odd = head
        even = head.next
        link_to_even_node = head.next

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = link_to_even_node
        return head
