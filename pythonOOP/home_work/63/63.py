# Однозв'язний список                                   Беспятий Дмитро

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"({self.data})"


class UserMenu:

    def __init__(self):
        self.head = None

    # 1 Додавання елементів у хвіст списку
    def app_end(self, data: int):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # 2 Додавання елементів до списку на початок
    def add_first(self, data):
        right = self.head
        node = Node(data)
        count = 0
        while right:
            if count == 0:
                self.head = node
                node.next = right
                count += 1
            else:
                right = right.next

    # 3 Вставити новий елемент із деяким значенням безпосередньо після елемента із даними, що є у списку.
    # Це завдання на додовання проміжного вузла.
    def app_middle(self, data, value):
        right = self.head
        left = self.head
        node = Node(value)
        while right:
            if left.data == data:
                node.next = right
                left.next = node
            left = right
            right = right.next

    # 4 Видалити елемент з хвоста списку
    def delete_last(self):
        current = prev = self.head
        if current.next is None:
            current = None
        else:
            while current:
                if current.next is None:
                    prev.next = None
                prev = current
                current = current.next

    # 5 Видалити елемент з голови списку
    def delete_first(self):
        current = self.head
        if current is None:
            print("Не має елемента для видалення")
        else:
            self.head = current.next

    # 6 Видалити елемент із деяким значенням у списку (задається якесь значення та кількість можливих видалень,
    # бо у списку дані можуть повторюватись).
    def delete_middle(self, data, value):
        right = self.head
        left = self.head
        node = Node(data)
        count = 0
        while right:
            if count < value:
                if right.data == data:
                    node = right.next
                    left.next = node
                    count += 1
            left = right
            right = right.next

    # 7 Замінити значення у списку на нове значення (користувач визначає, чи замінити тільки перше входження чи всі).
    def change(self, data, chan, value):
        right = self.head
        node = Node(chan)
        count = 0
        while right:
            if count < value == 1:
                if right.data == data:
                    right.data = node.data
                    count += 1
            if value != 1:
                if right.data == data:
                    right.data = node.data
            right = right.next

    # 8 Визначте розмір списку
    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def iter(self):
        current = self.head
        while current:
            print(current, end='->')
            current = current.next

    # 9 Показати вміст списк (прохід по всьому списку).
    def search(self):
        current = self.head
        while current:
            return current.data


menu = UserMenu()
menu.app_end(5)
menu.app_end(6)
menu.app_end(7)
menu.app_end(9)
menu.app_end(6)
menu.app_end(7)
menu.iter()
print()

menu.app_middle(7, 8)
menu.iter()
print()
menu.add_first(1)
menu.iter()
print()
menu.delete_middle(7, 1)
menu.iter()
print()
menu.change(6, 13, 2)
menu.iter()
