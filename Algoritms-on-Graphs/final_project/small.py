#!/usr/bin/python3


import sys
from heapq import heappop, heappush


class PriorityQueue:
    def __init__(self):
        self.H = []
        self.obsolete = set()

    def put(self, item):
        heappush(self.H, item)

    def get(self):
        self.obsolete.add(self.H[0][1])
        return heappop(self.H)[1]

    def empty(self):
        while self.H and self.H[0][1] in self.obsolete:
            heappop(self.H)
        return len(self.H) == 0
    
    def simple_get(self):
        return heappop(self.H)

    def last(self, imp):
        if self.empty():
            return False
        return self.H[0][0] < imp



class DistPreprocessSmall:
    def __init__(self, n, adj, cost):
        self.adj = adj
        self.cost = cost
        self.n = n
        self.inf = 2 * 10**6 * n
        self.rank = dict()
        self.preprocessd = set()

    def preprocess(self):
        rank = 1
        for v in range(self.n):
            self.rank[v] = rank
            rank += 1
            self.add_shortcuts(v)

    def filter_processed(self, v, u, side):
        return list(filter(lambda x: self.rank.get(x[1], self.n+1) > self.rank[v], zip(self.cost[side][u], self.adj[side][u])))

    def add_shortcuts(self, v):
        prev = self.filter_processed(v, v, 1)
        after = self.filter_processed(v, v, 0)
        limit = 0
        if prev:
            limit += max(prev)[0]
        if after:
            limit += max(after)[0]
        for cr, ur in prev:
            one_hop_back = self.filter_processed(v, ur, 1)
            if one_hop_back:
                l = limit - min(one_hop_back)[0]
            else:
                l = limit
            for c, u in after:
                if self.pre_dij(ur, u, v, l) > c + cr:
                    self.adj[0][ur].append(u)
                    self.cost[0][ur].append(c + cr)
                    self.adj[1][u].append(ur)
                    self.cost[1][u].append(c + cr)

    def pre_dij(self, s, t, v, l):
        dist = dict()
        q = PriorityQueue()
        dist[s] = 0
        q.put((0, s))
        while not q.empty():
            u = q.get()
            if u == t or dist[u] > l:
                break
            dist_u = dist[u]
            for c, v_ in self.filter_processed(v, u, 0):
                dist_v_ = dist.get(v_, self.inf)
                sum_ = dist_u + c
                if dist_v_ > sum_:
                    dist[v_] = sum_
                    q.put((sum_, v_))
        return dist.get(t, self.inf)

    def query(self, s, t):
        dist = [dict(), dict()]
        proc = [set(), set()]
        q = [PriorityQueue(), PriorityQueue()]
        estimate = self.inf
        dist[0][s] = 0
        dist[1][t] = 0
        q[0].put((0, s))
        q[1].put((0, t))
        flag = True
        while flag:
            flag = False
            if not q[0].empty():
                u = q[0].get()
                if dist[0][u] <= estimate:
                    self.process(u, dist, q, proc, 0)
                    flag = True
                if u in proc[1] and dist[0][u] + dist[1][u] < estimate:
                    estimate = dist[0][u] + dist[1][u]
            if not q[1].empty():
                ur = q[1].get()
                if dist[1][ur] <= estimate:
                    self.process(ur, dist, q, proc, 1)
                    flag = True
                if ur in proc[0] and dist[0][ur] + dist[1][ur] < estimate:
                    estimate = dist[0][ur] + dist[1][ur]
        return dist[0].get(t, -1)

    def process(self, u, dist, q, proc, side):
        dist_u = dist[side][u]
        for v, c in zip(self.adj[side][u], self.cost[side][u]):
            #if self.rank[v] < self.rank[u]:
            #    continue
            dist_v = dist[side].get(v, self.inf)
            sum_ = dist_u + c
            if dist_v > sum_:
                dist[side][v] = sum_
                q[side].put((sum_, v))
        proc[side].add(u)


def readl():
        return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n,m = readl()
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for e in range(m):
        u,v,c = readl()
        adj[0][u-1].append(v-1)
        cost[0][u-1].append(c)
        adj[1][v-1].append(u-1)
        cost[1][v-1].append(c)

    ch = DistPreprocessSmall(n, adj, cost)
    ch.preprocess()
    print("Ready")
    sys.stdout.flush()
    t, = readl()
    for i in range(t):
        s, t = readl()
        print(ch.query(s-1, t-1))
