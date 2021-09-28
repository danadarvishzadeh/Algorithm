
class DisjointSet:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, i):
        while self.parent[i] != i:
            i = self.parent[i]
        return i

    def union(self, i, j):
        id_i = self.find(i)
        id_j = self.find(j)
        if id_i == id_j:
            return
        if self.rank[id_i] > self.rank[id_j]:
            self.parent[id_j] = id_i
        else:
            self.parent[id_i] = id_j
            if self.rank[id_j] + 1 == self.rank[id_i]:
                self.rank[id_j] += 1
