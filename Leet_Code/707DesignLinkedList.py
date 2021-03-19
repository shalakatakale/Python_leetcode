'''# 707 Deign Linked list where you can get value at an index,
 add at head, add at tail, add at index, delete at index'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        current = self.head
        while index != 0:
            current = current.next
            index = index - 1
        return current.value

    def addAtHead(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    def addAtTail(self, value):
        new_node = Node(value)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def addAtIndex(self, index, value):
        if index < 0 or index > self.size:
            return  # or return -1
        elif index == 0:
            self.addAtHead(value)
        elif index == self.size:
            self.addAtTail(value)
        else:
            current = self.head
            while index - 1 != 0:
                current = current.next
                index = index - 1
            new_node = Node(value)

            new_node.next = current.next
            current.next.prev = new_node
            current.next = new_node
            new_node.prev = current

            self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return -1
        elif index == 0:
            current = self.head.next
            if current:
                current.prev = None

            self.head = current  # self.head.next
            self.size -= 1
            if self.size == 0:
                self.tail = None
        elif index == self.size - 1:
            current = self.tail.prev
            if current:
                current.next = None
            self.tail = current  # self.tail.prev
            self.size -= 1
            if self.size == 0:
                self.head = None
        else:
            current = self.head
            while index - 1 != 0:
                current = current.next
                index -= 1
            current.next = current.next.next
            current.next.prev = current
            self.size -= 1


LL = MyLinkedList()
LL.addAtHead(9)
LL.addAtTail(15)
LL.addAtTail(7)
LL.deleteAtIndex(0)
print(LL.get(1))
