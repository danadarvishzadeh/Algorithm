from queue import Queue as qu
import sys, threading

sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**30)  # new thread will get stack of such size


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1

def is_left_child(node):
    return node.data < node.parent.data

def promote_left(node):
    if is_left_child(node):
        node.parent.left = node.left
    else:
        node.parent.right = node.left
    if node.left:
        node.left.parent = node.parent

def promote_right(node):
    if is_left_child(node):
        node.parent.left = node.right
    else:
        node.parent.right = node.right
    node.right.parent = node.parent

def replace(node, x):
    if x.right:
        promote_right(x)
    if is_left_child(node):
        node.parent.left = x
    else:
        node.parent.right = x
    x.parent = node.parent
    if node.right != x:
        x.right = node.right
    if node.left is not None:
        x.left = node.left
        x.left.parent = x
    

def get_height(node):
    if node is None:
        return 0
    return node.height

def adjust_height(node):
    if node is not None:
        node.height = 1 + max(get_height(node.left), get_height(node.right))
    

class AVL:

    def __init__(self):
        self.root = None

    def insert(self, item):
        n = Node(item)
        found, place = self._find(item)
        if found:
            return
        if place is None:
            self.root = Node(item)
            return
        if place.data > item:
            place.left = n
        else:
            place.right = n
        n.parent = place
        self.rebalance(n)

    def delete(self, item):
        found, node = self._find(item)
        if not found:
            return
        if node == self.root:
            if node.right is None and node.left is None:
                self.root = None
            elif node.right is None:
                node.left.parent = None
                self.root = node.left
            elif node.left is None:
                node.right.parent = None
                self.root = node.right
        else:
            if node.right is None:
                promote_left(node)
            else:
                x = self.next(node)
                if x.parent != node:
                    m = x.parent
                else:
                    m = x
                replace(node, x)
                self.rebalance(m)

    def rebalance(self, node):
        p = node.parent
        if get_height(node.left) > get_height(node.right)+1:
            self.rebalance_right(node)
        elif get_height(node.left)+1 < get_height(node.right):
            self.rebalance_left(node)
        adjust_height(node)
        if p is not None:
            self.rebalance(p)

    def rebalance_left(self, node):
        m = node.right
        if get_height(m.left) > get_height(m.right):
            self.rotate_left(m)
            adjust_height(m)
            adjust_height(m.left)
        self.rotate_right(node)
        adjust_height(node)

    def rebalance_right(self, node):
        m = node.left
        if get_height(m.right) > get_height(m.left):
            self.rotate_right(m)
            adjust_height(m)
            adjust_height(m.right)
        self.rotate_left(node)
        adjust_height(node)

    def rotate_left(self, node):
        p = node.parent
        #if node is not root, update the parent
        if p is not None:
            if is_left_child(node):
                p.left = node.left
            else:
                p.right = node.left
            node.left.parent = p
        #if node is root, update root
        else:
            self.root = node.left
            node.left.parent = None
        #update node's parent and node's right's left
        node.parent = node.left
        right_child = node.parent.right
        #if node has the new root has right child, give them to node
        node.parent.right = node
        if right_child is not None:
            node.left = right_child
            right_child.parent = node
        else:
            node.left = None


    def rotate_right(self, node):
        p = node.parent
        #if node is not root, update the parent
        if p is not None:
            if is_left_child(node):
                p.left = node.right
            else:
                p.right = node.right
            node.right.parent = p
        #if node is root, update root
        else:
            self.root = node.right
            node.right.parent = None
        #update node's parent and node's right's left
        node.parent = node.right
        left_child = node.parent.left
        #if node has the new root has right child, give them to node
        node.parent.left = node
        if left_child is not None:
            node.right = left_child
            left_child.parent = node
        else:
            node.right = None

    def next(self, node):
        if node.right:
            current = node.right
            while current.left:
                current = current.left
            return current
        else:
            current = node
            #if node.data < current.data:
            #    return current
            while current.parent and current.parent.data < current.data:
                current = current.parent
            if current.parent:
                return current.parent
            else:
                return node

    def _find(self, item):
        if self.root is None:
            return False, None
        current = self.root
        while current.left or current.right:
            if item == current.data:
                return True, current
            if item < current.data:
                if current.left is None:
                    return False, current
                current = current.left
            else:
                if current.right is None:
                    return False, current
                current = current.right
        return (current.data == item), current

    def find(self, item):
        return self._find(item)[0]

    def range_sum(self, l, r):
        x = self._find(l)[1]
        if x is None or x.data < l:
            return 0
        summ = 0
        while x.data <= r:
            summ += x.data
            if x == self.next(x):
                break
            x = self.next(x)
        return summ
            
    def order(self):
        if self.root is None:
            print('empty')
            return
        s = [self.root]
        current = self.root
        while s:
            if current.left:
                current = current.left
                s.append(current)
            else:
                node = s.pop()
                print(node.data)
                if node.right:
                    s.append(node.right)
                    current = node.right

    def breath(self):
        if self.root is None:
            return ''
        res = []
        q = qu()
        q.put(self.root)
        while not q.empty():
            last = q.get()
            if last.left:
                q.put(last.left)
            if last.right:
                q.put(last.right)
            res.append((last.height, last.data))
        return res
        height = res[0][0]
        res.sort(key=lambda x: x[0], reverse=True)
        for r in res:
            if r[0] < height:
                print()
                print('- - - - - - - - - - - - - -')
                height -= 1
            print(r[1], end=' ')
        print()
        print(res)

def main():
    n = int(input())
    M = 1000000001
    x = 0
    answer = []
    tree = AVL()
    for _ in range(n):
        q = input().split()
        if q[0] == '+':
            tree.insert((int(q[1]) + x) % M)
        elif q[0] == '-':
            tree.delete((int(q[1]) + x) % M)
        elif q[0] == '?':
            if tree.find((int(q[1]) + x) % M):
                answer.append('Found')
                #print('Found')
            else:
                answer.append('Not found')
                #print('Not found')
        else:
            #answer.append((tree.breath(), x))
            x = tree.range_sum((int(q[1]) + x) % M, (int(q[2]) + x) % M)
            answer.append(x)
            #print(x)
    for a in answer:
        print(a)

if __name__ == "__main__":
    threading.Thread(target=main).start()
