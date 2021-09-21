#Uses python3

import sys

class Node:
    def __init__(self, data, i):
        self.data = data
        self.i = i


class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i-1) // 2

    def right(self, i):
        return (i*2) + 1

    def left(self, i):
        return (i*2) + 2

    def insert(self, data, i):
        node = Node(data, i)
        self.heap.append(node)
        i = len(self.heap) - 1
        self.sift_up(i)

    def sift_up(self, i):
        p = self.parent(i)
        while p >= 0 and self.heap[i].data > self.heap[p].data:
            self.swap(i, p)
            i = p
            p = self.parent(i)

    def swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def sift_down(self, i):
        maxindex = i
        size = len(self.heap)
        while True:
            tmp = maxindex
            l = self.left(maxindex)
            r = self.right(maxindex)
            if l < size and self.heap[l].data > self.heap[maxindex].data:
                maxindex = l
            if r < size and self.heap[r].data > self.heap[maxindex].data:
                maxindex = r
            if maxindex == tmp:
                break
            self.swap(maxindex, tmp)
            tmp = maxindex

    def extract_max(self):
        l = len(self.heap)
        if l == 1:
            return self.heap.pop().i
        else:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            m = self.heap.pop()
            self.sift_down(0)
            return m.i

    def topo_sort(self):
        sorted_graph = []
        while len(self.heap):
            sorted_graph.append(self.extract_max())
        return sorted_graph


def explore(vertex, pre, post, adj):
    global clock
    pre[vertex] = clock
    clock += 1
    for w in adj[vertex]:
        if not pre[w]:
            explore(w, pre, post, adj)
    post.insert(clock, vertex+1)
    clock += 1

def dfs(adj, n):
    global clock
    pre = [0 for _ in range(n)]
    post = MaxHeap()
    clock = 1
    for i in range(n):
        if not pre[i]:
            explore(i, pre, post, adj)
    return post.topo_sort()

def topologic_sort(adj, n):
    answer = dfs(adj, n)
    for _ in answer:
        print(_, end=' ')
    print()
     

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    topologic_sort(adj, n)
