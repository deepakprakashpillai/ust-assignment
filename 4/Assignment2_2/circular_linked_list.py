class CircularNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = CircularNode(value)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def display(self):
        values = []
        if not self.head:
            return values
        current = self.head
        while True:
            values.append(current.value)
            current = current.next
            if current == self.head:
                break
        return values

    def delete(self, value):
        if not self.head:
            return
        current = self.head
        prev = None
        while True:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    if current.next == self.head:
                        self.head = None
                    else:
                        self.head = current.next
                        last_node = self.head
                        while last_node.next != current:
                            last_node = last_node.next
                        last_node.next = self.head
                return
            prev = current
            current = current.next
            if current == self.head:
                break

cll = CircularLinkedList()

cll.append(100)
cll.append(200)
cll.append(300)

print("Circular Linked List:", cll.display()) 

cll.delete(200)
print("After deleting 200:", cll.display())