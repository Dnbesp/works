# -*- coding: utf-8 -*-
# Двозв'язний список                                   Беспятий Дмитро

# Реалізуйте клас двозв’язного списку, в якому передбачено:
# 1.	Додавання елемента до списку (в голову/в хвіст).
# 2.	Видалення елемента зі списку (з голови/з хвоста).
# 3.	Видалення елемента за значенням
# 4.	Додавання нового елемента за індексом.
# 5.	Прохід по всьому списку від голови до хвоста.
# 6.	Прохід по всьому списку від хвоста до голови.
# 7.	Повне очищення списку.

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
            self.head.prev = tail
            tail = tail.next
        tail.prev.next = None

    # 3. Видалення елемента за значенням і кількістю
    def del_cur(self, data, value):
        current = self.head
        count = 0
        while current:
            if count < value:
                if self.head.data == data:
                    self.head = current.next
                    count += 1
                else:
                    if current.data == data:
                        current.prev.next = current.next
                        current = current.next
                        count += 1
            if current:
                current = current.next

    # 4. Видалення елемента за індексом
    def del_index(self, inde):
        current = self.head
        count = 0
        while current:
            if count == inde:
                if count == 0:
                    self.head = current.next
                else:
                    current.prev.next = current.next
            if current:
                current = current.next
                count += 1

    # 5. Прохід по всьому списку від голови до хвоста
    def head_tail(self):
        current = self.head
        while current:
            current = current.next

    # 6. Реверс списку
    def tail_head(self):
        stack = []
        current = self.head
        while current is not None:
            stack.append(current.data)
            current = current.next
        current = self.head
        while current:
            current.data = stack.pop()
            current = current.next

    # 7. Повне очищення списку
    def del_all(self):
        current = self.head
        while current:
            current.prev = None
            current = current.next
        self.head = None
        self.tail = None
        print("Список порожній")


    def iter(self):
        current = self.head
        while current:
            print(current, end='->')
            current = current.next


menu = UserMenu()

while True:

    print("1. Додавання елементів до списку в голову")
    print("2. Додавання елементів до списку в хвіст")
    print("3. Видалення елемента зі списку з голови")
    print("4. Видалення елемента зі списку з хвоста")
    print("5. Видалення елемента за значенням і кількістю")
    print("6. Видалення елемента за індексом")
    print("7. Прохід по всьому списку від голови до хвоста")
    print("8. Прохід по всьому списку від хвоста до голови (реверс)")
    print("9. Повне очищення списку")
    print("0. Exit")

    cmd = int(input("Выберите пункт: "))

    if cmd == 1:
        data = int(input("Введіть число: "))
        menu.app_begin(data)
        menu.iter()
        print()
    if cmd == 2:
        data = int(input("Введіть число: "))
        menu.app_end(data)
        menu.iter()
        print()
    if cmd == 3:
        menu.del_head()
        menu.iter()
        print()
    if cmd == 4:
        menu.del_tail()
        menu.iter()
        print()
    if cmd == 5:
        data = int(input("Введіть число: "))
        value = int(input("Введіть кількість: "))
        menu.del_cur(data, value)
        menu.iter()
        print()
    if cmd == 6:
        inde = int(input("Введіть індекс: "))
        menu.del_index(inde)
        menu.iter()
        print()
    if cmd == 7:
        menu.head_tail()
        menu.iter()
        print()
    if cmd == 8:
        menu.tail_head()
        menu.iter()
        print()
    if cmd == 9:
        menu.del_all()
        menu.iter()
        print()
    if cmd == 0:
        break
    print()