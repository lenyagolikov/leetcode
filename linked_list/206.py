# https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def __init__(self, value=0, next=None) -> bool:
        self.value = value
        self.next = next


class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        """Return a reverse linked list

        speed: O(n)
        memory: O(1)

        head: ListNode
        rtype: ListNode
        """
        prev = None
        current = head

        while current:
            next = current.next
            current.next = prev

            prev = current
            current = next

        return prev
