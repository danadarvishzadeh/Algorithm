class Heap:

    def __init__(self, size, default_):
        self.size = size
        self.heap = [[default_, i] for i in range(self.size)]

    def parent(self, i):
        return i // 2 - 1

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def sift_down(self, i):
        maxindex = i
        l = self.left_child(i)
        if l < self.size and self.heap[l][0] <= self.heap[maxindex][0]:
            if self.heap[l][0] == self.heap[maxindex][0]:
                if self.heap[l][1] < self.heap[maxindex][1]:
                    maxindex = l
            else:
                maxindex = l
            
        r = self.right_child(i)
        if r < self.size and self.heap[r][0] <= self.heap[maxindex][0]:
            if self.heap[r][0] == self.heap[maxindex][0]:
                if self.heap[r][1] < self.heap[maxindex][1]:
                    maxindex = r
            else:
                maxindex = r
        if maxindex != i:
            self.heap[i], self.heap[maxindex] = self.heap[maxindex], self.heap[i]
            self.sift_down(maxindex)

    def get_min(self):
        return self.heap[0]

    def add_to_min(self, value):
        self.heap[0][0] += value
        self.sift_down(0)


class Thread:

    def __init__(self):
        self.n_w, self.n_p = map(int, input().split())
        self.processes = list(map(int, input().split()))
        self.h = Heap(self.n_w, 0)
        self.result = []

    def assign_jobs(self):
        for i in range(self.n_p):
            finished, worker_id = self.h.get_min()
            self.h.add_to_min(self.processes[i])
            self.result.append((worker_id, finished))
    
    def results(self):
        for i, j in self.result:
            print(i, j, sep=' ')


if __name__ == "__main__":
    t = Thread()
    t.assign_jobs()
    t.results()
