# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

class ListNode:
    def __init__(self, value=0, next=None) -> None:
        self.value = value
        self.next = next


class Solution:
    def remove_duplicates(self, head: ListNode) -> ListNode:
        """Remove all duplicates of a sorted linked list and return linked list sorted as well"""
        current = head

        while current and current.next:
            if current.value == current.next.value:
                current.next = current.next.next
            else:
                current = current.next

        return head
