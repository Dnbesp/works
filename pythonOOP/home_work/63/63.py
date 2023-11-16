# Однозв'язний список                                   Беспятий Дмитро

class UserMenu:

    def __init__(self):
        self.head = None

    def app_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
