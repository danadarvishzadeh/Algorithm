import sys, threading
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)

class TreeHeight:
    def read(self):
        self.n = int(input())
        self.parent = list(map(int, input().split()))
        self.heights = [1 if self.parent[i] == -1 else 0 for i in range(self.n)]

    def height(self):
        for i in range(self.n):
            height = self.compute(i)
        return max(self.heights)


    def compute(self, i):
        if self.heights[i]:
            return self.heights[i]
        h = self.compute(self.parent[i]) + 1
        self.heights[i] = h
        return h


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.height())
threading.Thread(target=main).start()
