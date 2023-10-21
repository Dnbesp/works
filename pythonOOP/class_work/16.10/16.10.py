class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class Stack:
    def __init__(self, max_size=-1):
        self.head = None
        self.max_size = max_size

    # def size(self):
    #     return (self.max_size + 1)

    def push(self, data):
        if self.max_size == 0:
            raise Exception("Stack is overflow")
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            value = self.head.data
            self.head = self.head.next
            self.max_size += 1
            return value

    def is_empty(self):
        return self.head is None

    def iter(self):
        current = self.head
        while current:
            if current.next is None:
                print(current, end='')
                break
            print(current, "->", end=' ')
            current = current.next

    def peak(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            value = self.head.data
            return value


stack = Stack(max_size=3)
stack.push(5)
stack.push(6)
stack.push(7)
stack.iter()

