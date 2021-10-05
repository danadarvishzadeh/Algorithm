#!/usr/bin/python3

import sys
from heapq import heappop, heappush


class CustomePriorityQueue:
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
        return not bool(self.H)


class Graph:
    def __init__(self, n, adj, cost):
        self.n = n
        self.inf = n*10**6 
        self.adj = adj[0]
        self.adjr = adj[1]
        self.cost = cost[0]
        self.costr = cost[1]

    def initialise(self, s, t):
        self.dist = dict()
        self.distr = dict()
        self.proc = set()
        self.procr = set()
        self.q = CustomePriorityQueue()
        self.qr = CustomePriorityQueue()

        self.dist[s] = 0
        self.distr[t] = 0
        self.q.put((0, s))
        self.qr.put((0, t))

    def dijkstra(self, s, t):
        self.initialise(s, t)
        while not self.q.empty() and not self.qr.empty():
            u = self.q.get()
            self.process(self.adj[u], self.cost[u], u)
            if u in self.procr:
                return self.shortest_path()
            ur = self.qr.get()
            self.processr(self.adjr[ur], self.costr[ur], ur)
            if ur in self.proc:
                return self.shortest_path()
        return -1

    def process(self, adj, cost, u):
        dist_u = self.dist[u]
        for v, c in zip(adj, cost):
            dist_v = self.dist.get(v, self.inf)
            s = dist_u + c
            if dist_v > s:
                self.dist[v] = s
                self.q.put((s, v))
        self.proc.add(u)

    def processr(self, adjr, costr, ur):
        distr_u = self.distr[ur]
        for v, c in zip(adjr, costr):
            distr_v = self.distr.get(v, self.inf)
            s = distr_u + c
            if distr_v > s:
                self.distr[v] = s
                self.qr.put((s, v))
        self.procr.add(ur)

    def shortest_path(self):
        min_ = self.inf
        for u in self.proc:
            dist_u = self.dist.get(u, self.inf)
            distr_u = self.distr.get(u, self.inf)
            s = dist_u + distr_u
            if min_ > s:
                min_ = s
        for u in self.procr:
            dist_u = self.dist.get(u, self.inf)
            distr_u = self.distr.get(u, self.inf)
            s = dist_u + distr_u
            if min_ > s:
                min_ = s
        return min_


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
    t, = readl()
    graph = Graph(n, adj, cost)
    for i in range(t):
        s, t = readl()
        if s == t:
            print(0)
        else:
            print(graph.dijkstra(s-1, t-1))
