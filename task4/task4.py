class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() == 0:
            return None
        return self.stack.pop(0)

    def push(self, value):
        self.stack.insert(0, value)

    def peek(self):
        if self.size() == 0:
            return None
        return self.stack[0]

    def tail_pop(self):
        if self.size() == 0:
            return None
        return self.stack.pop()

    def tail_push(self, value):
        self.stack.append(value)

    def tail_peek(self):
        if self.size() == 0:
            return None
        return self.stack[-1]
