class RingBuffer:
    def __init__(self, capacity):
        self.data = []
        self.capacity = capacity
        self.max = self.capacity
        self.oldest = 0

    def append(self, item):
        if len(self.data) != self.max:
            self.data.append(item)

        else:
            print("self.oldest is", self.oldest)
            self.data.pop(self.data[self.oldest])
            self.data.insert(self.oldest, item)
            if self.oldest < self.max - 1:
                self.oldest += 1
            else:
                self.oldest = 0

    def get(self):
        return self.data
