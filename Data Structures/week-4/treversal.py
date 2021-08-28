
class Node:

    def __init__(self, s):
        s = list(map(int, s.split()))
        self.key = s[0]
        self.right = s[2]
        self.left = s[1]

    def __str__(self):
        return str(self.key)


class Tree:

    def __init__(self, nodes):
        self.tree = [Node(s) for s in nodes]
        self.root = self.tree[0]

    def traversal(self):
        s = []
        pre = []
        ino = []
        post = []
        s.append([self.root, 1])
        while s:
            if s[-1][1] == 1:
                pre.append(s[-1][0].key)
                s[-1][1] = 2
                if s[-1][0].left != -1:
                    s.append([self.tree[s[-1][0].left], 1])
            elif s[-1][1] == 2:
                ino.append(s[-1][0].key)
                s[-1][1] = 3
                if s[-1][0].right != -1:
                    s.append([self.tree[s[-1][0].right], 1])
            elif s[-1][1] == 3:
                post.append(s[-1][0].key)
                s.pop()
        return ino, pre, post
                

if __name__ == "__main__":
    n = int(input())
    nodes = [input() for _ in range(n)]
    tree = Tree(nodes)
    l = tree.traversal()
    for i in l:
        print(' '.join(list(map(str, i))))

