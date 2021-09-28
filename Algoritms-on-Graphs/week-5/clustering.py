#Uses python3
import sys
import math

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

def compute_weight(a, b):
    first = a[0] - b[0]
    second = a[1] - b[1]
    return math.sqrt(first**2 + second**2)

def cluster(x, y):
    X = []
    n = len(x)
    s = DisjointSet(n)
    points = [(a, b) for a, b in zip(x, y)]
    edges = []
    for a in range(n):
        for b in range(a+1, n):
            edges.append((a, b, compute_weight(points[a], points[b])))
    edges.sort(key=lambda x: x[2])
    unions = 0
    for u, v, w in edges:
        if unions < n:
            if s.find(u) != s.find(v):
                X.append(w)
                s.union(u, v)
                unions += 1
        else:
            break
    return sorted(X, reverse=True)

def clustering(x, y, k):
    paths = cluster(x, y)
    if paths:
        return paths[k-2]
    return -1.


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
