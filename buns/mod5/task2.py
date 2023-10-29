class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Error")

        if self.head == self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
        else:
            value = self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None

        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Error")
        return self.tail.value

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count