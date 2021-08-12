# https://leetcode.com/problems/remove-linked-list-elements/

class ListNode:
    def __init__(self, value=0, next=None) -> None:
        self.value = value
        self.next = next


class Solution:
    def remove_elements(self, head: ListNode, value: int) -> ListNode:
        """Remove all the nodes of the linked list has Node.val == val, and return a new head"""
        barrier = ListNode(0)
        barrier.next = head

        current = barrier

        while current.next:
            if current.next.value == value:
                current.next = current.next.next
            else:
                current = current.next

        return barrier.next
