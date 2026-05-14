class Stack:
    def __init__(self, _track_min=True):
        self.stack = []
        self.min_stack = Stack(_track_min=False) if _track_min else None
        self._sum = 0

    def size(self):
        return len(self.stack)

    def peek(self):
        return self.stack[0] if self.stack else None

    def push(self, value):
        self.stack.insert(0, value)
        if self.min_stack is None or not isinstance(value, (int, float)):
            return
        self._sum += value
        current_min = self.min_stack.peek()
        new_min = value if current_min is None or value < current_min else current_min
        self.min_stack.push(new_min)

    def pop(self):
        if not self.stack:
            return None
        value = self.stack.pop(0)
        if not isinstance(value, (int, float)):
            return value
        self._sum -= value
        if self.min_stack is not None:
            self.min_stack.pop()
        return value

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

    def get_min(self):
        return self.min_stack.peek() if self.min_stack is not None else None

    def get_mean(self):
        if not self.stack:
            return None
        return self._sum / len(self.stack)
