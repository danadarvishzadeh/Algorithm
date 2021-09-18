
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.size = 0

class SPlay:

    def __init__(self):
        self.root = None

    def _find(self, index):
        current = self.root
        while current:
            s = get_size(current.left)
            if s == index:
                break
            elif s > index:
                if current.left:
                    current = current.left
                else:
                    break
            else:
                if current.right:
                    index -= s + 1
                    current = current.right
                else:
                    break
        return current

    def find(self, index):
        node = self._find(index)
        self.splay(node)
        return node

    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            self.root.parent, node.left = node, self.root
            self.make_root(node)
        adjust_size(node)

    def make_root(self, node):
        if node is None:
            return
        self.root, node.parent = node, None

    def rotate_right(self, node):
        if node.parent:
            if node.parent.right == node:
                node.parent.right, node.left.parent = node.left, node.parent
            else:
                node.parent.left, node.left.parent = node.left, node.parent
        else:
            self.make_root(node.left)
            #self.root, node.left.parent = node.left, None
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
            if gp:
                if gp.left == p:
                    if p.left == node:
                        self.rotate_right(gp)
                        self.rotate_right(p)
                    else:
                        self.rotate_left(p)
                        self.rotate_right(gp)
                else:
                    if p.left == node:
                        self.rotate_right(p)
                        self.rotate_left(gp)
                    else:
                        self.rotate_left(gp)
                        self.rotate_left(p)
                adjust_size(gp)
            elif p.left == node:
                self.rotate_right(p)
            else:
                self.rotate_left(p)
            adjust_size(p)
            adjust_size(node)

    def order(self):
        current = self.root
        output = ''
        if current is None:
            return output
        s = [self.root]
        while s:
            if current.left:
                s.append(current.left)
                current = current.left
            else:
                last = s.pop()
                output += last.data
                if last.right:
                    s.append(last.right)
                    current = last.right
        return output
    
def create_tree(string):
    tree = SPlay()
    for letter in string:
        tree.insert(letter)
    return tree


def adjust_size(node):
    if node is None:
        return
    node.size = get_size(node.left) + get_size(node.right) + 1

def get_size(node):
    if node is None:
        return 0
    return node.size

def find_max(root):
    while root and root.right:
        root = root.right
    return root

def merge(s1, s2):
    if s1 is None or s1.root is None:
        return s2
    elif s2 is None or s2.root is None:
        return s1
   #print('s1:', s1.order())
   #print('s2:', s2.order())
    T = find_max(s1.root)
    s1.splay(T)
    T.right, s2.root.parent = s2.root, T
    adjust_size(T)
    return s1

def cut_left(s, index):
    s.find(index)
    if s.root is None:
        return None, None
    new_s = SPlay()
    new_s.make_root(s.root.left)
    s.root.left = None
    adjust_size(s.root)
    adjust_size(new_s.root)
    return new_s, s

def cut_right(s, index):
    s.find(index)
    if s.root is None:
        return None, None
    new_s = SPlay()
    new_s.make_root(s.root.right)
    s.root.right = None
    adjust_size(s.root)
    adjust_size(new_s.root)
    return s, new_s

def solve(tree, i, j, k):
    #the moving part
    moving, right = cut_right(tree, j)
    left, moving = cut_left(moving, i)
    #print('\nleft:', left.order())
    #print('moving:', moving.order())
    #print('right:', right.order())
    remaining = merge(left, right)
    #print('remaining:', remaining.order())
    if remaining.root and remaining.root.size == k:
        left, right = cut_right(remaining, k)
    else:
        left, right = cut_left(remaining, k)
    tree = merge(left, moving)
    tree = merge(tree, right)
    #print('tree:', tree.order())
    return tree

if __name__ == "__main__":
    string = input()
    tree = create_tree(string)
    for _ in range(int(input())):
        i, j, k = map(int, input().split())
        tree = solve(tree, i, j, k)
    print(tree.order())
