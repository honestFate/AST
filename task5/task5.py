class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        return None

    def size(self):
        return len(self.queue)
