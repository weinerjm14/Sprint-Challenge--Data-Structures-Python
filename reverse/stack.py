class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        return self.storage.append(value)

    def pop(self):
        if self.size == 0:
            return None
        if self.size > 0:
            self.size -= 1
            return self.storage.pop()
