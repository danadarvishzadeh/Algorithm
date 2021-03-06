#!/usr/bin/python3


import sys
from heapq import heappop, heappush
import time


class PriorityQueue:
    def __init__(self):
        self.H = []
        self.obsolete = set()

    def put(self, item):
        heappush(self.H, item)

    def get(self):
        self.obsolete.add(self.H[0][1])
        return heappop(self.H)[1]

    def __bool__(self):
        while self.H and self.H[0][1] in self.obsolete:
            heappop(self.H)
        return len(self.H) > 0
    
    def simple_get(self):
        return heappop(self.H)[1]
    
    def last(self, node):
        if self.H:
            return node <= self.H[0][0]
        return True


class DistPreprocessSmall:
    def __init__(self, n, adj, cost):
        self.n = n
        self.inf = n * 2 * 10**6
        self.adj = adj[0]
        self.adjr = adj[1]
        self.cost = cost[0]
        self.costr = cost[1]
        self.shortcut_added = 0
        self.order = dict()
        self.rank = dict()
        self.level = dict()
        self.bidi = False
        self.debug = False

    def order_initialisation(self, queue):
        for node in range(self.n):
            self.update_order(node)
            queue.put((self.order[node], node))

    def update_order(self, node):
        ed, sc = self.edge_difference(node)
        cn = self.contracted_neighbors(node)
        l = self.level.get(node, 0)
        self.order[node] = 1*ed + 1*sc + 1*cn + 1*l

    def update_level(self, node):
        for u in self.adj[node]:
            self.level[u] = max(self.level.get(u, 0), self.level.get(node, 0)+1)

    def contracted_neighbors(self, node):
        contracted = 0
        for neighbor in self.adj[node] + self.adjr[node]:
            if self.rank.get(neighbor, 0) < self.rank.get(node, 0):
                contracted += 1
        return contracted

    def edge_difference(self, node):
        self.shortcuts_to_be_added = []
        s = 0
        cover = set()
        next_edges = self.couple_edges(0, node, node)
        previous_edges = self.couple_edges(1, node, node)
        limit = 0
        if next_edges:
            limit = max(next_edges)[0]
        for s_cost , start in previous_edges:
            limit += s_cost
            witness_path = self.dijkstra(start, limit=limit, ignore=node)
            for e_cost, end in next_edges:
                shortcut_cost = s_cost + e_cost
                if witness_path.get(end, self.inf) > shortcut_cost:
                    self.shortcuts_to_be_added.append((start, end, shortcut_cost))
                    s += 1
                    cover.add(start)
                    cover.add(end)
        return s - len(self.adj[node]) - len(self.adjr[node]), len(cover)

    def preprocess(self):
        queue = PriorityQueue()
        self.order_initialisation(queue)
        rank = 1
        while queue:
            v = queue.simple_get()
            self.rank[v] = rank
            rank += 1
            self.update_order(v)
            if not queue.last(self.order[v]):
                queue.put((self.order[v], v))
                rank -= 1
                del self.rank[v]
                continue
            if self.shortcuts_to_be_added:
                for s in self.shortcuts_to_be_added:
                    self.add_shortcut(s[0], s[1], s[2])
            self.update_level(v)
        if self.debug:
            #self.debug_graph()
            self.debug_added_edges()

    def add_shortcut(self, start, end, weight):
        self.adj[start].append(end)
        self.adjr[end].append(start)
        self.cost[start].append(weight)
        self.costr[end].append(weight)
        self.shortcut_added += 1

    def couple_edges(self, side, node, filter_=None):
        if side == 0:
            coupled = list(zip(self.cost[node], self.adj[node]))
        else:
            coupled = list(zip(self.costr[node], self.adjr[node]))
        if filter_ is not None:
            coupled = list(filter(lambda x: self.compare(x[1], filter_), coupled))
        return coupled

    def compare(self, node, filter_):
        if self.rank.get(node, 0) == 0:
            return node != filter_
        return self.rank.get(node, 0) > self.rank.get(filter_, 0)

    def dijkstra(self, start, end=None, ignore=None, limit=False):
        dist = [dict()]
        q = [PriorityQueue()]
        dist[0][start] = 0
        q[0].put((0, start))
        if self.bidi:
            dist.append(dict())
            q.append(PriorityQueue())
            proc = [set(), set()]
            dist[1][end] = 0
            q[1].put((0, end))
            proc[0].add(start)
            proc[1].add(end)
            estimate = self.inf
        if ignore is not None:
            finding = set(list(filter(lambda x: self.compare(x, ignore), self.adj[ignore])))
            found = len(finding)
        while any(q):
            if self.bidi:
                flag = False
            if q[0]:
                u = q[0].get()
                if self.bidi:
                    if dist[0][u] <= estimate:
                        self.process(u, 0, dist[0], q[0], proc[0])
                        flag = True
                    if u in proc[1] and dist[0][u] + dist[1][u] < estimate:
                        estimate = dist[0][u] + dist[1][u]
                else:
                    if limit is not None and dist[0][u] > limit:
                        break
                    if end is not None and u == end:
                        break
                    if ignore is not None:
                        if found == 0:
                            break
                        if u in finding:
                            found -= 1
                    self.process(u, 0, dist[0], q[0], ignore=ignore)
            if self.bidi and q[1]:
                ur = q[1].get()
                if dist[1][ur] <= estimate:
                    self.process(ur, 1, dist[1], q[1], proc[1])
                    flag = True
                if ur in proc[0] and dist[0][ur] + dist[1][ur] < estimate:
                    estimate = dist[0][ur] + dist[1][ur]
            if self.bidi and not flag:
                break
        if self.bidi:
            return -1 if estimate == self.inf else estimate
        elif end is not None:
            return dist[0].get(end, self.inf)
        else:
            return dist[0]
                    

    def process(self, node, side, dist, queue, proc=None, ignore=None):
        node_cost = dist[node]
        for cost, end in self.couple_edges(side, node, ignore):
            if ignore == None:
                if self.rank[end] < self.rank[node]:
                    continue
            end_cost = dist.get(end, self.inf)
            if end_cost > cost + node_cost:
                dist[end] = cost + node_cost
                queue.put((cost + node_cost, end))
        if proc:
            proc.add(node)

    def debug_contraction(self, through, start, end, weight):
        print(f"contracting {through+1}\n{start+1}--{weight}-->{end+1}")

    def debug_graph(self):
        for u in range(self.n):
            for v, c in zip(self.adj[u], self.cost[u]):
                print(u, v, c)

    def debug_added_edges(self):
        print(f"----- added {self.shortcut_added} shortcuts -----")

    def debug_switch(self):
        self.debug = True

    def query(self, s, t):
        self.bidi = True
        return self.dijkstra(s, t)


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
    #ch.debug_switch()
    ch.preprocess()
    print("Ready")
    sys.stdout.flush()
    t, = readl()
    for i in range(t):
        s, t = readl()
        print(ch.query(s-1, t-1))
