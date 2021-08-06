from collections import deque


class PacketsQueue(deque):
    
    def __init__(self):
        maxlen, self.packet_num = map(int, input().split())
        super().__init__(maxlen=maxlen)
        self.last = None
        self.result = [-2 for i in range(self.packet_num)]
        self.recive()
    
    def empty(self):
        return len(self) == 0

    def full(self):
        return len(self) == self.maxlen

    def available(self):
        return len(self) < self.maxlen

    def done(self):
        p = self.popleft()
        self.result[p[2]] = p[1]

    def get(self, item, i):
        arriving, processing = list(map(int, item.split()))
        if self.last and arriving == self.last[0] and self.last[1] != 0 and self.full():
            self.drop(i)
        else:
            while not self.empty() and self[0][0] <= arriving:
                self.done()
            if self.available():
                if self.empty():
                    start = arriving
                else:
                    start = self[-1][0]
                self._append(start, processing, i)
                self.last = arriving, processing
            else:
                self.drop(i)

    def recive(self):
        for i in range(self.packet_num):
            self.get(input(), i)

    def show_result(self):
        while not self.empty():
            self.done()
        for i in self.result:
            print(i)

    def drop(self, i):
        self.result[i] = -1

    def _append(self, s, p, i):
        super().append((s+p, s, i))

if __name__ == "__main__":
    queue = PacketsQueue()
    queue.show_result()
