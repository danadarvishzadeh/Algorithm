#Uses python3

import sys

def explore(vertex, pre, post, adj):
    pre[vertex] = True
    for w in adj[vertex]:
        if not pre[w]:
            if explore(w, pre, post, adj):
                return 1
        elif pre[w] and not post[w]:
            return 1
    post[vertex] = True


def dfs(adj, n):
    pre = [False for _ in range(n)]
    post = [False for _ in range(n)]
    for i in range(n):
        if not pre[i] and not post[i]:
            if explore(i, pre, post, adj):
                return 1
    return 0

def reach(adj, n):
    return dfs(adj, n)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(reach(adj, n))
