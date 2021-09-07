
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.left_sum = 0
        self.right_sum = 0
        self.height = 1
        self.parent = None


class AVL:
    def __init__(self):
        self.root = None

    def _find(self, key):
        if self.root is None:
            return None
        current = self.root
        while True:
            if current.data == key:
                return current
            elif current.data > key:
                if current.left:
                    current = current.left
                else:
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    break
        return current

    def find(self, key):
        node = self._find(key)
        if node and node.data == key:
            return 1
        return 0

    def next(self, node):
        current = node
        if current.right:
            current = current.right
            while current.left:
                current = current.left
        elif current.parent:
            while current.parent and current.data > current.parent.data:
                current = current.parent
            current = current.parent
        if current == node:
            return None
        return current

    def insert(self, key):
        position = self._find(key)
        node = Node(key)
        if position is None:
            self.root = node
            return
        elif position.data == key:
            return
        elif position.data < key:
            position.right, node.parent = node, position
        else:
            position.left, node.parent = node, position
        self.rebalance(position)

    def delete(self, key):
        node = self._find(key)
        #tree is empty
        if node is None:
            return
        #node does not exists
        elif node.data != key:
            return
        else:
            #node does not have a right subtree
            if node.right is None:
                #tree only has root
                if node.parent is None and node.left is None:
                    self.root = None
                #node is root and tree has some other node on the left
                elif node.parent is None:
                    node.left.parent, self.root = None, node.left
                #node is not root but does not have any child
                elif node.left is None:
                    if node.parent.right == node:
                        node.parent.right = None
                    else:
                        node.parent.left = None
                    self.rebalance(node)
                else:
                    #node has a left subtree and parent
                    if node.parent.right == node:
                        node.left.parent, node.parent.right = node.parent, node.left
                    else:
                        node.left.parent, node.parent.left = node.parent, node.left
                    self.rebalance(node)
            else:
                #node is in the middle of tree and need a replace
                next_element = self.next(node)
                if next_element.parent == node:
                    next_element_parent = next_element
                else:
                    next_element_parent = next_element.parent
                self.replace(node, next_element)
                self.rebalance(next_element_parent)

    def rotate_right(self, node):
        if node.parent:
            if node.parent.right == node:
                node.parent.right, node.left.parent = node.left, node.parent
            else:
                node.parent.left, node.left.parent = node.left, node.parent
        else:
            self.root, node.left.parent = node.left, None
        excess = node.left.right
        node.parent, node.left.right = node.left, node
        if excess:
            excess.parent, node.left = node, excess
        else:
            node.left = None

    def rotate_left(self, node):
        if node.parent:
            if node.parent.right == node:
                node.parent.right, node.right.parent = node.right, node.parent
            else:
                node.parent.left, node.right.parent = node.right, node.parent
        else:
            self.root, node.right.parent = node.right, None
        excess = node.right.left
        node.parent, node.right.left = node.right, node
        if excess:
            excess.parent, node.right = node, excess
        else:
            node.right = None

    def rebalance(self, node):
        while node:
            if self.gg(node.left) + 1 < self.gg(node.right):
                r = node.right
                if self.gg(r.left) > self.gg(r.right):
                    self.rotate_right(r)
                    self.adjust_height(r)
                    self.adjust_sum(r)
                self.rotate_left(node)
            if self.gg(node.left) > self.gg(node.right) + 1:
                l = node.left
                if self.gg(l.left) < self.gg(l.right):
                    self.rotate_left(l)
                    self.adjust_height(l)
                    self.adjust_sum(l)
                self.rotate_right(node)
            self.adjust_height(node)
            self.adjust_sum(node)
            node = node.parent

    def gg(self, node):
        if node is None:
            return 0
        return node.height

    def adjust_height(self, node):
        node.height = 1 + max(self.gg(node.left), self.gg(node.right))

    def ss(self, node):
        if node is None:
            return 0
        return node.data + node.left_sum + node.right_sum

    def adjust_sum(self, node):
        node.left_sum = self.ss(node.left)
        node.right_sum = self.ss(node.right)

    def replace(self, node, next_element):
        #promoting right subtree of the next element
        if next_element.right:
            right_subtree = next_element.right
            if next_element == next_element.parent.right:
                right_subtree.parent, next_element.parent.right = next_element.parent, right_subtree
            else:
                right_subtree.parent, next_element.parent.left = next_element.parent, right_subtree
        else:
            if next_element.parent.right == next_element:
                next_element.parent.right = None
            else:
                next_element.parent.left = None
        #the actual repalcing
        if node.parent is not None:
            if node == node.parent.right:
                node.parent.right, next_element.parent = next_element, node.parent
            else:
                node.parent.left, next_element.parent = next_element, node.parent
        else:
            next_element.parent, self.root = None, next_element
        #attaching left child
        if node.left:
            node.left.parent, next_element.left = next_element, node.left
        #attaching right child
        if node.right and node.right != next_element:
            node.right.parent, next_element.right = next_element, node.right

    def order(self):
        current = self.root
        if current is None:
            return
        s = [self.root]
        while s:
            if current.left:
                s.append(current.left)
                current = current.left
            else:
                last = s.pop()
                print(last.data)
                if last.right:
                    s.append(last.right)
                    current = last.right

    def rsum(self, l, r):
        if self.root is None:
            return 0
        start, end = self._find(l), self._find(r)
        s, e = start, end
        before_start_sum, before_end_sum = start.left_sum, end.left_sum
        while s.parent:
            if s.parent.right == s:
                before_start_sum += s.parent.left_sum + s.parent.data
            s = s.parent
        while e.parent:
            if e.parent.right == e:
                before_end_sum += e.parent.left_sum + e.parent.data
            e = e.parent
        summ = end.data + before_end_sum - before_start_sum
        if start.data < l:
            summ -= start.data
        if end.data > r:
            summ -= end.data
        return summ


def main():
    n = int(input())
    M = 1000000001
    x = 0
    answer = []
    tree = AVL()
    #with open('4_set_range_sum/tests/36', 'r') as f:
    #with open('q.txt', 'r') as f:
        #n, *f = f.read().splitlines()
    #for _ in range(int(n)):
    for _ in range(n):
        q = input().split()
        #q = f[_].split()
        #print(f"query number{_}")
        #print(f"query: {q}")
        #print(f"next query: {f[_+1]}")
        #print()
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
            x = tree.rsum((int(q[1]) + x) % M, (int(q[2]) + x) % M)
            answer.append(x)
            #print(x)
    for a in answer:
        print(a)

if __name__ == "__main__":
    main()
