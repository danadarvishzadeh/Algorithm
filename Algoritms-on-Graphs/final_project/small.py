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
        self.adj = adj[0]
        self.adjr = adj[1]
        self.cost = cost[0]
        self.costr = cost[1]
        self.inf = 2 * 10**6 * n
        self.contracted = dict()
        self.rank = dict()
        self.cover = dict()
        self.node_order = dict()

    def compute_importance(self, v):
        ed = self.edge_difference(v)
        nc = self.contracted.get(v, 0)
        sc = self.cover.get(v, 0)
        nl = self.node_order.get(v, 0)
        return ed + nc + sc + nl

    def preprocess(self):
        q = PriorityQueue()
        shortcut_count = 1
        for v in range(n):
            self.add_shortcut(v)

    def edge_difference(self, v):
        count = 0
        limit = 0
        cover = set()
        if self.cost[v]:
            limit += max(self.cost[v])
        if self.costr[v]:
            limit += max(self.costr[v])
        for ur, cr in zip(self.adjr[v], self.costr[v]):
            cover.add(ur)
            for u, c in zip(self.adj[v], self.cost[v]):
                cover.add(u)
                if self.costr[u]:
                    l = limit - min(self.costr[u])
                else:
                    l = limit
                if self.preprocess_dijkstra(ur, u, v, l) > c + cr:
                    count += 1
        self.cover[v] = len(cover)
        return count - len(self.adj[v]) - len(self.adjr[v])

    def add_shortcut(self, v):
        limit = 0
        if self.cost[v]:
            limit += max(self.cost[v])
        if self.costr[v]:
            limit += max(self.costr[v])
        for ur, cr in zip(self.adjr[v], self.costr[v]):
            for u, c in zip(self.adj[v], self.cost[v]):
                if self.costr[u]:
                    l = limit - min(self.costr[u])
                else:
                    l = limit
                if self.preprocess_dijkstra(ur, u, v, l) > c + cr:
                    self.adj[ur].append(u)
                    self.cost[ur].append(c+cr)
                    self.adjr[u].append(ur)
                    self.costr[u].append(c+cr)

    def update_node_order(self, v):
        for u in self.adj[v]:
            self.node_order[u] = self.node_order.get(v, 0) + 1
        for u in self.adjr[v]:
            self.node_order[u] = self.node_order.get(v, 0) + 1

    def contracted_neighbors(self, v):
        cn = 0
        for u in self.adj[v]:
            cn += self.contracted.get(u, 0)
        for u in self.adjr[v]:
            cn += self.contracted.get(u, 0)
        return cn

    def preprocess_dijkstra(self, s, t, v, limit):
        dist = dict()
        q = PriorityQueue()
        dist[s] = 0
        q.put((0, s))
        while not q.empty():
            u = q.get()
            if dist[u] > limit:
                break
            if u == v:
                continue
            self.p_process(u, v, q, dist)
            if u == t:
                break
        return dist.get(t, self.inf)

    def p_process(self, u, r, q, dist):
        for v, c in zip(self.adj[u], self.cost[u]):
            if v == r:
                continue
            dist_v = dist.get(v, self.inf)
            sum_ = dist[u] + c
            if dist_v > sum_:
                dist[v] = sum_
                q.put((sum_, v))


    def process(self, u):
        for v, c in zip(self.adj[u], self.cost[u]):
            dist_v = self.dist.get(v, self.inf)
            sum_ = self.dist[u] + c
            if dist_v > sum_:
                self.dist[v] = sum_
                self.q.put((sum_, v))

    def processr(self, ur):
        for v, c in zip(self.adjr[ur], self.costr[ur]):
            distr_v = self.distr.get(v, self.inf)
            sum_ = self.distr[ur] + c
            if distr_v > sum_:
                self.distr[v] = sum_
                self.qr.put((sum_, v))

    def initialise(self, s, t):
        self.dist = dict()
        self.distr = dict()
        self.proc = set()
        self.procr = set()
        self.q = PriorityQueue()
        self.qr = PriorityQueue()

        self.dist[s] = 0
        self.distr[t] = 0
        self.q.put((0, s))
        self.qr.put((0, t))

    def query(self, s, t):
        self.initialise(s, t)
        estimate = self.inf
        flag = 1
        while flag:
            flag = 0
            if not self.q.empty():
                u = self.q.get()
                if self.dist[u] < estimate:
                    self.process(u)
                    flag = 1
                    self.proc.add(u)
                dist_u = self.dist.get(u, self.inf)
                distr_u = self.distr.get(u, self.inf)
                if u in self.procr and dist_u + distr_u < estimate:
                    estimate = dist_u + distr_u
            if not self.qr.empty():
                ur = self.qr.get()
                if self.distr[ur] < estimate:
                    self.processr(ur)
                    flag = 1
                    self.procr.add(ur)
                dist_ur = self.dist.get(ur, self.inf)
                distr_ur = self.distr.get(ur, self.inf)
                if ur in self.proc and dist_ur + distr_ur < estimate:
                    estimate = dist_ur + distr_ur

        return -1 if estimate == self.inf else estimate

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
