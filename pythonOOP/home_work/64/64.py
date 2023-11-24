# -*- coding: utf-8 -*-
# Двозв'язний список                                   Беспятий Дмитро
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f"({self.data})"

class UserMenu:

    def __init__(self):
        self.head = None
        self.tail = None

    # 1. Додавання елементів до списку в голову
    def app_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        new_node.prev = None
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    # додавання в хвіст
    def app_end(self, data):
        new_node = Node(data)
        new_node.next = None
        tail = self.head
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        while tail.next is not None:
            tail = tail.next
        tail.next = new_node
        new_node.prev = tail

    # 2. Видалення елемента зі списку з голови
    def del_head(self):
        self.head = self.head.next

    # Видалення елемента зі списку з хвоста
    def del_tail(self):
        tail = self.head
        while tail.next is not None:
            tail = tail.next
        # tail.next = None
        # self.head.prev = None


    def iter(self):
        current = self.head
        while current:
            print(current, end='->')
            current = current.next


menu = UserMenu()
menu.app_begin(5)
menu.app_begin(6)
menu.app_begin(7)
menu.app_begin(9)
menu.app_begin(6)
menu.app_begin(7)
menu.iter()
print()

menu.app_end(7)
menu.app_end(9)
menu.app_end(6)
menu.app_end(7)
menu.iter()
print()

menu.del_head()
menu.iter()
print()

menu.del_tail()
menu.iter()