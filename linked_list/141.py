# https://leetcode.com/problems/linked-list-cycle/

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def has_cycle(self, head: ListNode) -> bool:
        """Return True, if linked list has a cycle. Otherwise, return False.

        speed: O(n)
        memory: O(n)

        head: ListNode
        rtype: bool
        """
        temp = set()

        while head:
            if head.next not in temp:
                temp.add(head.next)
            else:
                return True
            head = head.next

        return False


class Solution:
    def has_cycle(self, head: ListNode) -> bool:
        """Floyd's tortoise and hare: race. 
        Return True, if linked list has a cycle. Otherwise, return False.

        speed: O(n)
        memory: O(1)

        head: ListNode
        rtype: bool
        """
        if not head:
            return False

        slow = fast = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False
