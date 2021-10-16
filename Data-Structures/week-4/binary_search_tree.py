
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

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


class BST:

    def __init__(self):
        self.root = None

    def insert(self, item):
        if self.root is None:
            self.root = Node(item)
            return
        n = Node(item)
        place = self.find(item)
        if place.data > item:
            place.left = n
        else:
            place.right = n
        n.parent = place

    def delete(self, item):
        node = self.find(item)
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
                replace(node, x)

    def next(self, node):
        if node.right:
            current = node.right
            while current.left:
                current = current.left
            return current
        else:
            if node.data >= node.parent.data:
                return None
            current = node.parent
            while current.parent and current.parent.data > current.data:
                current = current.right
            return current

    def find(self, item):
        current = self.root
        while current.left or current.right:
            if item == current.data:
                return current
            if item < current.data:
                if current.left is None:
                    return current
                current = current.left
            else:
                if current.right is None:
                    return current
                current = current.right
        return current

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

