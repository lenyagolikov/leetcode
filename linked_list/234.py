# https://leetcode.com/problems/palindrome-linked-list/

class ListNode:
    def __init__(self, value=0, next=None) -> None:
        self.value = value
        self.next = next


class Solution:
    def is_palindrome(self, head: ListNode) -> bool:
        """Return True if linked list is a palindrome. Otherwise, return False"""
        middle = self.middle_node(head)
        reverse = self.reverse_list(middle)

        while reverse:
            if reverse.value != head.value:
                return False
            reverse = reverse.next
            head = head.next

        return True

    def middle_node(self, head: ListNode) -> ListNode:
        """Return middle node of the linked list"""
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    def reverse_list(self, head: ListNode) -> ListNode:
        """Return a reverse linked list"""
        prev = None
        current = head

        while current:
            next = current.next
            current.next = prev

            prev = current
            current = next

        return prev
