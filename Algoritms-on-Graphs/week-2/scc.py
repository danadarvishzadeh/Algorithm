#Uses python3

import sys

def explore(vertex, adj, pre, post, clock):
    stack = [vertex]
    while stack:
        current = stack[-1]
        if not pre[current]:
            pre[current] = clock
            clock += 1
            for v in adj[current]:
                if not pre[v]:
                    stack.append(v)
        elif not post[current]:
            post[current] = clock
            clock += 1
            stack.pop()
        else:
            stack.pop()
    return clock
    #global clock
    #pre[vertex] = clock
    #clock += 1
    #for w in adj[vertex]:
    #    if not pre[w]:
    #        explore(w, adj, pre, post)
    #post[vertex] = clock
    #clock += 1

def simple_explore(vertex, adj, visited, post, timer):
    stack = [vertex]
    while stack:
        current = stack[-1]
        if not visited[current]:
            visited[current] = True
            post[current] = 0
            timer += 1
            for v in adj[current]:
                if not visited[v]:
                    stack.append(v)
        else:
            stack.pop()
    #visited[vertex] = True
    #post[vertex] = 0
    #timer += 1
    #for v in adj[vertex]:
    #    if not visited[v]:
    #        timer = simple_explore(v, adj, visited, post, timer)
    return timer

def dfs(adj, n):
    pre = [0 for _ in range(n)]
    post = [0 for _ in range(n)]
    clock = 1
    for i in range(n):
        if not pre[i]:
            clock = explore(i, adj, pre, post, clock)
    return post

def scc(adj, rev_adj, n):
    post = dfs(rev_adj, n)
    visited = [False for _ in range(n)]
    sccs = 0
    timer = 0
    while timer < n:
        i = post.index(max(post))
        timer = simple_explore(i, adj, visited, post, timer)
        sccs += 1
    return sccs

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    rev_adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        rev_adj[b - 1].append(a - 1)
    print(scc(adj, rev_adj, n))
