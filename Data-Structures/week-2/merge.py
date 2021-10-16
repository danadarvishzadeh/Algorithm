import sys, threading

sys.setrecursionlimit(10**6)
threading.stack_size(2**27)

class Set_:
    
    def __init__(self):
        self.n_t, self.n_q = map(int, input().split())
        self.tables = list(map(int, input().split()))
        self.queries = [map(int, input().split()) for _ in range(self.n_q)]
        self.parent = []
        self.rank = []
        self.max_rank = 0
        self.make_set()

    def make_set(self):
        for i in range(self.n_t):
            self.parent.append(i)
        for j in self.tables:
            self.rank.append(j)
            self.max_rank = max(self.max_rank, j)

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_id = self.find(i-1)
        j_id = self.find(j-1)
        if i_id == j_id:
            pass
        else:
            self.parent[i_id] = j_id
            self.rank[j_id] += self.rank[i_id]
            self.rank[i_id] = 0
            self.max_rank = max(self.max_rank, self.rank[j_id])
        print(self.max_rank)

    def work(self):
        for destination, source in self.queries:
            self.union(source, destination)



def main():
    s = Set_()
    s.work()
threading.Thread(target=main).start()
