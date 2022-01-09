class Stack:
    def __init__(self):
        # Stack dynamic array implementation
        self.stack = []
        self.length = 0

    def push(self, item):
        self.stack.append(item)
        self.length += 1

    def pop(self):
        if self.isEmpty():
            return None
        self.length -= 1
        return self.stack.pop()

    def peek(self):
        return None if self.isEmpty() else self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def __str__(self):
        return str(self.stack)


# s = Stack()
# print(s.isEmpty())
# print(s.peek())
# s.push(1)
# s.push(2)
# s.push(3)
# print(s)
# s.pop()
# print(s)
# print(s.peek())
# print(s.isEmpty())
