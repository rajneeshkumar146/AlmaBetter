class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def getFirst(self):
        return self.head.val

    def getLast(self):
        return self.tail.val

    def getNodeAt(self, index):
        curr = self.head
        while index > 0:
            curr = curr.next
            index -= 1

        return curr

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        node = self.getNodeAt(index)
        return node.val

    # addFirst
    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

        self.size += 1

    # addTail
    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.size += 1

    # addAt(index)
    def addAtIndex(self, index: int, val: int) -> None:

    def deleteFirst(self):

    def deleteLast(self):

    # DeleteAt(index)
    def deleteAtIndex(self, index: int) -> None:
