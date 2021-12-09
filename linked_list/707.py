# https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self) -> None:
        self.head = Node(-1)
        self.size = 0

    def get(self, index: int) -> int:
        current = self.head.next
        i = 0
        while current:
            if i == index:
                return current.val
            i += 1
            current = current.next
        return -1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return -1
        new_node = Node(val)
        current = self.head

        for _ in range(index):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return -1

        current = self.head
        for _ in range(index):
            current = current.next

        current.next = current.next.next
        self.size -= 1
