class Deque:
    def __init__(self):
        self.deque = []
        self._min = None

    def addFront(self, item):
        self.deque.insert(0, item)
        self._track_min_added(item)

    def addTail(self, item):
        self.deque.append(item)
        self._track_min_added(item)

    def removeFront(self):
        if not self.deque:
            return None
        item = self.deque.pop(0)
        self._track_min_removed(item)
        return item

    def removeTail(self):
        if not self.deque:
            return None
        item = self.deque.pop()
        self._track_min_removed(item)
        return item

    def _track_min_added(self, item):
        if self._min is None or item < self._min:
            self._min = item

    def _track_min_removed(self, item):
        if not self.deque:
            self._min = None
            return
        if item == self._min:
            self._min = min(self.deque)

    def get_min(self):
        return self._min

    def size(self):
        return len(self.deque)

