class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, data):
        node = Node(data)
        if self._size == 0:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def dequeue(self):
        if self._size == 0:
            raise IndexError
        node = self._head
        self._head = node.next
        self._size -= 1
        if self._size == 0:
            self._tail = None
        return node.data

    @property
    def size(self):
        return self._size

    def iter(self):
        current = self._head
        while current:
            if current.next is None:
                print(current, end='')
                break
            print(current, "->", end=' ')
            current = current.next


queue = Queue()
queue.enqueue(2)
queue.enqueue(4)
queue.enqueue(1)
queue.enqueue(7)
queue.iter()
print()
print(queue.dequeue())
queue.iter()
print()
print(queue.size)