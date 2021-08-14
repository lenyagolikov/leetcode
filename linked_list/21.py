# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    def __init__(self, value=0, next=None) -> None:
        self.value = value
        self.next = next


class Solution:
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Merge two sorted linked list and return it as a sorted list"""
        result = ListNode(0)
        current = result

        while l1 and l2:
            if l1.value <= l2.value:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        current.next = l1 if l1 else l2

        return result.next
