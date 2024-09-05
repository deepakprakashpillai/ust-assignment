class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = QueueNode(value)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_node.value

    def peek(self):
        return self.front.value if self.front else None

    def is_empty(self):
        return self.front is None

    def display(self):
        values = []
        current = self.front
        while current:
            values.append(current.value)
            current = current.next
        return values

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue:", queue.display())
print("Front value:", queue.peek())
print("Dequeued value:", queue.dequeue())
print("Queue after dequeuing:", queue.display())