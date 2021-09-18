
class Node:
    def __init__(self, data):
        self.data = data
        self.size = 0
        self.left = None
        self.right = None
        self.parent = None


class Rope:
    def __init__(self, string):
        self.root = None
        self.build_tree(string)

    def build_tree(self, string):
        for i in string:
            self.insert(i)

    def insert(self, data):
        node = Node(data)
        root = self.root
        if root:
            root.parent = node
            node.left = root
        self.root = node
        self.update(node)
        
    def _find(self, index):
        node = self.root
        while node:
            s = self.get_size(node.left)
            if s == index:
                return node
            elif s > index:
                node = node.left
            else:
                node = node.right
                index -= s + 1
        return node

    def get_size(self, node):
        if node is None:
            return 0
        return self.get_size(node.left) + self.get_size(node.right) + 1

    def find(self, index):
        node = self._find(index)
        self.splay(node)
        return node

    def splay(self, node):
        p = node.parent
        gp = p.parent
        if gp:
            if gp.left == p:
                if p.left == node:
                    self.rotate_right(gp)
                    self.rotate_right(p)
                else:
                    self.rotate_left(p)
                    self.rotate_right(gp)
            else:
                if p.right == node:
                    self.rotate_left(gp)
                    self.rotate_left(p)
                else:
                    self.rotate_right(p)
                    self.rotate_left(gp)
            self.upadte(gp)
        if p:
            if p.left == node:
                self.rotate_right(p)
            else:
                self.rotate_left(p)
        self.update(p)
        self.update(node)

    def update(self, node):
        self.size = self.get_size(node)

    def rotate_right(self, node):
        p = node.parent
        l = node.left
        axil = l.right
        if p:
            if p.left == node:
                p.left, l.parent = l, p
            else:
                p.right, l.parent = l, p
        else:
            self.root, l.parent = l, None
        node.parent, l.right = l, node
        if axil:
            node.left, axil.parent = axil, p
        else:
            node.left = None

    def rotate_left(self, node):
        p = node.parent
        r = node.right
        axil = r.left
        if p:
            if p.left == node:
                p.left, r.parent = r, p
            else:
                p.right, r.parent = r, p
        else:
            self.root, r.parent = r, None
        node.parent, r.left = r, node
        if axil:
            node.right, axil.parent = axil, p
        else:
            node.right = None


    def split(self, tree, index):
        if tree.root is None:
            return (None, None)
        tree.find(index)
        right = tree.root
        left = right.left
        right.left, left.parent = None, None
        left_tree, right_tree = Rope(), Rope()
        left_tree.root, right_tree.root = left, right
        left_tree.update(left)
        right_tree.update(right)
        return (left_tree, right_tree)

    def merge(left, right):
        tree = Rope()
        if left.root is None:
            return right
        elif right.root is None:
            return left
        middle = left.find(left.root.size)
        middle.right = right.root
        middle.right.parent = middle
        tree.root = middle
        tree.update(middle)
        return tree
    
    def order(self):
        output = ''
        if self.root:
            node = self.root
            stack = [node]
            while stack:
                if node.left:
                    stack.append(node.left)
                    node = node.left
                else:
                    tmp = stack.pop()
                    output += tmp.data
                    if tmp.right:
                        stack.append(tmp.right)
                        node = tmp.right
        return output

    def solve(self, queries):
        for i, j, k in queries:
           
        return self.order()
