#Uses python3

import sys

def explore(vertex, visited, cc, c):
    visited[vertex] = True
    cc[vertex] = c
    for w in adj[vertex]:
        if not visited[w]:
            explore(w, visited, cc, c)

def dfs(adj, n):
    visited = [False for _ in range(n)]
    cc = [0 for _ in range(n)]
    c = 1
    for i in range(n):
        if not visited[i]:
            explore(i, visited, cc, c)
            c += 1
    return cc

def reach(adj, n):
    cc = dfs(adj, n)
    return max(cc)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, n))
