class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

def check_balanced_brackets(input_string):
    stack = Stack()
    opening_brackets = {'(': ')', '{': '}', '[': ']'}
    closing_brackets = {')': '(', '}': '{', ']': '['}

    for char in input_string:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return False
            top_element = stack.pop()
            if opening_brackets[top_element] != char:
                return False

    return stack.is_empty()

print(check_balanced_brackets("()"))
print(check_balanced_brackets("()[]{}"))
print(check_balanced_brackets("(]"))
print(check_balanced_brackets("([)]"))
print(check_balanced_brackets("{[]}"))
