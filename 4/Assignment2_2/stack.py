class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = StackNode(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        popped_node = self.top
        self.top = self.top.next
        return popped_node.value

    def peek(self):
        return self.top.value if self.top else None

    def is_empty(self):
        return self.top is None

    def display(self):
        values = []
        current = self.top
        while current:
            values.append(current.value)
            current = current.next
        return values

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Stack:", stack.display())
print("Top value:", stack.peek())
print("Popped value:", stack.pop())
print("Stack after popping:", stack.display())

