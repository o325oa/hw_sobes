# 1 Задание

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

# 2 Задание
def is_balanced(expression):
    stack = []
    opening_brackets = set(['(', '[', '{'])
    closing_brackets = set([')', ']', '}'])
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack[-1] != bracket_pairs[char]:
                return "Несбалансированно"
            stack.pop()

    return "Сбалансированно" if not stack else "Несбалансированно"

# Примеры
print(is_balanced("(((([{}]))))"))
print(is_balanced("[([])((([[[]]])))]{()}")) #
print(is_balanced("{{[()]}"))
print(is_balanced("}{"))
