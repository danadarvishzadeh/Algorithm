
class Node:

    def __init__(self, key, data):
        self.data = data
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

def next(node):
    if node.right or node.parent:
        if node.right:
            node = node.right
            while node.left:
                node = node.left
        else:
            while node.parent and node.data > node.parent.data:
                node = node.parent
            node = node.parent
        return node
    else:
        return None

def find_max(root):
    while root.right:
        root = root.right
    return root

def merge(s1, s2):
    T = find_max(s1)
    s1.splay(T)
    T.right, s2.root.parent = s2.root, T

def split(s, key):
    s.find(key)
    if s.root is None:
        return None, None
    elif s.root.key == key:
        s1 = SPlay()
        s1.make_root(s.left)
        s.make_root(s.right)
        return s, s1
    elif s.root.key < key:
        s1 = SPlay()
        s1.make_root(s.right)
        s.root.right = None
        return s, s1
    else:
        s1 = SPlay()
        s1.make_root(s.left)
        s.root.left = None
        return s, s1


class SPlay:

    def __init__(self):
        self.root = None

    def _find(self, key):
        current = self.root
        while current:
            if current.key == key:
                return current
            elif current.key > key:
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
        self.splay(node)
        return node

    def insert(self, key, data):
        position = self._find(key)
        node = Node(key, data)
        if position is None:
            self.root = node
        elif position.data == data:
            return
        elif position.data < data:
            position.right, node.parent = node, position
        else:
            position.left, node.parent = node, position
        self.splay(node)

    def make_root(self, node):
        self.root, node.parent = node, None

    def delete(self, key):
        node = self._find(key)
        if node.key != key:
            return
        self.splay(next(node))
        self.splay(node)
        if node.right:
            if node.left:
                node.left.parent, node.right.left = node.right, node.left
            self.make_root(node.right)
        else:
            if node.left:
                self.make_root(node.left)
            else:
                self.root = None

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
            self.make_root(node.right)
            #self.root, node.right.parent = node.right, None
        excess = node.right.left
        node.parent, node.right.left = node.right, node
        if excess:
            excess.parent, node.right = node, excess
        else:
            node.right = None

    def splay(self, node):
        while node and node.parent:
            p = node.parent
            gp = node.parent.parent
            if p.left == node:
                self.rotate_right(p)
            else:
                self.rotate_left(p)
            if gp:
                if gp.left == node:
                    self.rotate_right(gp)
                else:
                    self.rotate_left(gp)

    def order(self):
        current = self.root
        xxx = []
        if current is None:
            return xxx
        s = [self.root]
        while s:
            if current.left:
                s.append(current.left)
                current = current.left
            else:
                last = s.pop()
                xxx.append(last.data)
                if last.right:
                    s.append(last.right)
                    current = last.right
        return xxx
