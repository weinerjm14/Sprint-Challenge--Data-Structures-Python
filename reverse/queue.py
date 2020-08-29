from collections import deque


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = deque([])

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        return self.storage.append(value)

    def dequeue(self):
        if self.size == 0:
            return None
        if self.size > 0:
            self.size -= 1
            return self.storage.popleft()
