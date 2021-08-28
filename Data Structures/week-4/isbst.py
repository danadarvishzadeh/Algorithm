import sys, threading

sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**30)  # new thread will get stack of such size


class Node:
    def __init__(self, s):
        s = list(map(int, s.split()))
        self.data = s[0]
        self.l = s[1]
        self.r = s[2]


def is_bst_helper(node, tree, mini, maxi):
    if node == -1:
        return True
    data = tree[node]
    l = tree[node].l
    r = tree[node].r
    #print(f"{data.data} >= {maxi} and {data.data} < {mini}")
    if data.data > maxi or data.data < mini:
        return False
    return is_bst_helper(l, tree, mini, data.data-1) and is_bst_helper(r, tree, data.data+1, maxi)


def is_bst(tree):
    if tree:
        return is_bst_helper(0, tree, -4294967296, 4294967296)
    return True

def main():
    n = int(input())
    nodes = [Node(input()) for _ in range(n)]
    if is_bst(nodes):
        print('CORRECT')
    else:
        print('INCORRECT')


if __name__ == "__main__":
    threading.Thread(target=main).start()
