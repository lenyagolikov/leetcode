# https://leetcode.com/problems/middle-of-the-linked-list/

class ListNode:
    def __init__(self, value=0, next=None) -> bool:
        self.value = value
        self.next = next


class Solution:
    def middle_node(self, head: ListNode) -> ListNode:
        """Return the middle node of the linked list.
        If there are two middle nodes, return the second middle node.

        speed: O(n)
        memory: O(n)

        head: ListNode
        rtype: ListNode
        """
        temp = []

        while head:
            temp.append(head)
            head = head.next

        return temp[len(temp) // 2]


class Solution:
    def middle_node(self, head: ListNode) -> ListNode:
        """Return the middle node of the linked list.
        If there are two middle nodes, return the second middle node.

        speed: O(n)
        memory: O(1)

        head: ListNode
        rtype: ListNode
        """
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
