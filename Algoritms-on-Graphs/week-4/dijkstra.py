#Uses python3
from math import inf
import sys

class PriorityQueue:
    def __init__(self, n):
        self.H = []
        self.check = [False for _ in range(n)]

    def parent(self, i):
        return (i-1) // 2

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    def swap(self, i, j):
        self.H[i], self.H[j] = self.H[j], self.H[i]

    def sift_up(self, i):
        p = self.parent(i)
        while i > 0 and self.H[p][0] > self.H[i][0]:
            self.swap(i, p)
            i = p
            p = self.parent(i)

    def sift_down(self, i):
        minindex = i
        s = len(self.H)
        while True:
            l = self.left(minindex)
            r = self.right(minindex)
            if l < s and self.H[l][0] < self.H[minindex][0]:
                minindex = l
            if r < s and self.H[r][0] < self.H[minindex][0]:
                minindex = r
            if minindex == i:
                break
            self.swap(i, minindex)
            i = minindex

    def insert(self, p, i):
        self.H.append((p, i))
        self.sift_up(len(self.H)-1)

    def extract_min(self):
        while True:
            if self.empty():
                return None
            self.swap(0, len(self.H)-1)
            m = self.H.pop()
            self.sift_down(0)
            if not self.check[m[1]]:
                break
        self.check[m[1]] = True
        return m[1]

    def empty(self):
        return len(self.H) == 0


def dijkstra(adj, cost, s):
    n = len(adj)
    dist = [inf for _ in range(n)]
    dist[s] = 0
    q = PriorityQueue(n)
    q.insert(0, s)
    while True:
        u = q.extract_min()
        if u is None:
            break
        for v, c in zip(adj[u], cost[u]):
            if dist[v] > dist[u] + c:
                dist[v] = dist[u] + c
                q.insert(dist[v], v)
    return dist

def distance(adj, cost, s, d):
    dist = dijkstra(adj, cost, s)
    if dist[d] != inf:
        return dist[d]
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, d = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, d))
