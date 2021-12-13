# https://leetcode.com/problems/copy-list-with-random-pointer/

from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def deep_copy_random_list(self, head: Optional[Node]) -> Optional[Node]:
        """
        Construct a deepcopy of the linked list
        Time Complexity: O(n) - 1 pass
        Space Complexity: O(n)
        """
        result = Node(head.val) if head else None
        link_to_result = result
        hashmap = {head: result}

        while head:
            if head.next:
                if head.next in hashmap:
                    result.next = hashmap[head.next]
                else:
                    result.next = Node(head.next.val)
                    hashmap[head.next] = result.next
            if head.random:
                if head.random in hashmap:
                    result.random = hashmap[head.random]
                else:
                    result.random = Node(head.random.val)
                    hashmap[head.random] = result.random
            result = result.next
            head = head.next

        return link_to_result


class Solution:
    def deep_copy_random_list(self, head: Optional[Node]) -> Optional[Node]:
        """
        Construct a deepcopy of the linked list
        Time Complexity: O(n) - 2 passes
        Space Complexity: O(n)
        """
        result = {None: None}

        current = head
        while current:
            result[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            result[current].next = result[current.next]
            result[current].random = result[current.random]
            current = current.next

        return result[head]


class Solution:
    def deep_copy_random_list(self, head: Optional[Node]) -> Optional[Node]:
        """
        Construct a deepcopy of the linked list
        Time Complexity: O(n) - 2 passes
        Space Complexity: O(1)
        """
        copy = node = Node(0)

        while head:
            node.next = Node(head.val, None, head.random)
            node = node.next
            head.random = node
            head = head.next

        node = copy
        while node:
            if node.random:
                node.random = node.random.random
            node = node.next
        return copy.next
