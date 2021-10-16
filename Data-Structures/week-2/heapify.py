
class Heap:

    def __init__(self):
        self.max_size = int(input())
        self.heap = list(map(int, input().split()))
        self.ops = []

    def parent(self, i):
        return i // 2 - 1

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def sift_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            p = self.parent(i)
            self.ops.append((i, p))
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p

    def sift_down(self, i):
        maxindex = i
        l = self.left_child(i)
        if l < self.max_size and self.heap[l] < self.heap[maxindex]:
            maxindex = l
        r = self.right_child(i)
        if r < self.max_size and self.heap[r] < self.heap[maxindex]:
            maxindex = r
        if maxindex != i:
            self.ops.append((i, maxindex))
            self.heap[i], self.heap[maxindex] = self.heap[maxindex], self.heap[i]
            self.sift_down(maxindex)

    def heapify(self):
        for i in range(self.max_size // 2, -1, -1):
            self.sift_down(i)

    def show_ops(self):
        print(len(self.ops))
        for i, j in self.ops:
            print(i, j, sep=' ')

    def sorted(self):
        print(self.heap)

if __name__ == "__main__":
    h = Heap()
    h.heapify()
    h.show_ops()
