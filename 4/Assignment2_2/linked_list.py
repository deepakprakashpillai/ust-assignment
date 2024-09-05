class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values

    def delete(self, value):
        current = self.head
        previous = None
        while current and current.value != value:
            previous = current
            current = current.next
        if current is None:
            return
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

ll = LinkedList()

ll.append(1)
ll.append(2)
ll.append(3)

print("Basic Linked List:", ll.display())

ll.delete(2)
print("After deleting 2 :", ll.display())