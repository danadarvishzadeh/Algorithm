#Uses python3

import sys
import queue
from math import inf

def bfs(adj, q):
    infinit = [0 for _ in range(len(adj))]
    while not q.empty():
        u = q.get()
        if not infinit[u]:
            infinit[u] = 1
        for v in adj[u]:
            if not infinit[v]:
                q.put(v)
    return infinit

def find_shortest_paths(adj, cost, s):
    n = len(adj)
    dist = [inf for _ in range(n)]
    dist[s] = 0
    q = queue.Queue()
    for _ in range(n-1):
        for u in range(n):
            for v, c in zip(adj[u], cost[u]):
                if dist[v] > dist[u] + c:
                    dist[v] = dist[u] + c
    for u in range(n):
        for v, c in zip(adj[u], cost[u]):
            if dist[v] > dist[u] + c:
                dist[v] = dist[u] + c
                q.put(u)
    infinit = bfs(adj, q)
    return infinit, dist
    

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
    s = data[0]
    s -= 1
    infinit, dist = find_shortest_paths(adj, cost, s)
    for x in range(n):
        if infinit[x] == 1:
            print('-')
        elif dist[x] == inf:
            print('*')
        else:
            print(dist[x])

