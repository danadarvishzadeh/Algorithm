#!/usr/bin/python3

import sys
import math
from heapq import heappop, heappush

class CustomePriorityQueue:
    def __init__(self):
        self.H = []
        self.obsolete = set()

    def put(self, item):
        heappush(self.H, item)

    def custome_get(self):
        try:
            u = heappop(self.H)
            while u in self.obsolete:
                u = heappop(self.H)
            self.obsolete.add(u[1])
        except:
            return None
        return u[1]


class Graph:
    def __init__(self, n, adj, cost, x, y):
        self.n = n
        self.inf = n*10**6 
        self.adj = adj[0]
        self.adjr = adj[1]
        self.cost = cost[0]
        self.costr = cost[1]
        self.x = x
        self.y = y

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

    def query(self, s, t):
        self.initialise(s, t)
        while True:
            u = self.q.custome_get()
            if u is None:
                break
            self.process(self.adj[u], self.cost[u], u, s, t)
            if u in self.procr:
                return self.shortest_path()
            ur = self.qr.custome_get()
            if ur is None:
                break
            self.processr(self.adjr[ur], self.costr[ur], ur, s, t)
            if ur in self.proc:
                return self.shortest_path()
        return -1

    def process(self, adj, cost, u, s, t):
        dist_u = self.dist[u]
        for v, c in zip(adj, cost):
            pi = self.p(v, s, t)
            dist_v = self.dist.get(v, self.inf)
            sum_ = dist_u + c
            if dist_v > sum_:
                self.dist[v] = sum_
                self.q.put((sum_+pi, v))
        self.proc.add(u)

    def processr(self, adjr, costr, ur, s, t):
        distr_u = self.distr[ur]
        for v, c in zip(adjr, costr):
            pi = self.pr(v, s, t)
            distr_v = self.distr.get(v, self.inf)
            sum_ = distr_u + c
            if distr_v > sum_:
                self.distr[v] = sum_
                self.qr.put((sum_+pi, v))
        self.procr.add(ur)

    def compute_pi(self, a, b):
        return math.sqrt(((self.x[a] - self.x[b])**2) + ((self.y[a] - self.y[b])**2))

    def p(self, a, s, t):
        return (self.compute_pi(a, t) - self.compute_pi(a, s)) / 2

    def pr(self, a, s, t):
        return (self.compute_pi(a, s) - self.compute_pi(a, t)) / 2

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
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for i in range(n):
        a, b = readl()
        x[i] = a
        y[i] = b
    for e in range(m):
        u,v,c = readl()
        adj[0][u-1].append(v-1)
        cost[0][u-1].append(c)
        adj[1][v-1].append(u-1)
        cost[1][v-1].append(c)
    t, = readl()
    graph = Graph(n, adj, cost, x, y)
    for i in range(t):
        s, t = readl()
        if s == t:
            print(0)
        else:
            print(graph.query(s-1, t-1))
