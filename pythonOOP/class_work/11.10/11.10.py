class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data}, {self.next.data if self.next else None})"


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def append_at_a_location(self, data: int, value):
        right = self.head
        left = self.head
        node = Node(value)
        while right:
            if right.data == data and self.head.data != data:
                node.next = right
                left.next = node
            left = right
            right = right.next

    def del_first_node(self):
        current = self.head
        if current is None:
            print("No data element to delete")
        else:
            self.head = current.next

    def del_last_node(self):
        #коли є тільки голова не видаляється fix
        current = prev = self.head
        while current:
            if current.next is None:
                prev.next = None
            prev = current
            current = current.next

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def __contains__(self, deta):
        return self.search(deta)

    def iter(self):
        current = self.head
        while current:
            print(current, end='-->')
            current = current.next

    def __iter__(self):
        print("Call __iter__")
        self.temp = self.head
        return self
        # current = self.head
        # while current:
        #     yield current.data
        #     current = current.next

    def __next__(self):
        if self.temp:
            result = self.temp.data
            self.temp = self.temp.next
            return result
        raise StopIteration



lst = LinkedList()
lst.del_first_node()
lst.append(8)
lst.append(6)
lst.append(4)
lst.append(2)
for x in iter(lst):
    print(x, end=' ')
# for x in lst:
#     print(x)
# # lst.iter()
# print()
# print(lst.search(4), lst.search(5))
# print(4 in lst, 5 in lst)
# print("Довжина списку=", len(lst))
# # lst.append_at_a_location(4, 5)
# lst.del_first_node()
# lst.del_last_node()
# lst.del_last_node()
# lst.iter()
# print()
# print(f"{lst.head=}")



# n1 = Node(8)
# n2 = Node(6)
# n3 = Node(4)
# n4 = Node(2)
#
# n1.next = n2
# n2.next = n3
# n3.next = n4

# current = n1
# while current:
#     print(current.data, end=' ')
#     current = current.next
#
# print(id(8), id(6), id(4), id(2))
