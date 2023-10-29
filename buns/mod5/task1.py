class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def print_stack(self):
        current = self.head
        print(current.data)
        while current.next:
            current = current.next
            print(current.data)



stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(5)
stack.print_stack()  # Вывод: 3 2 1
stack.pop()
print(stack.peek()) # 3


