# python3
import sys
from queue import Queue

class SuffixTreeNode:
    def __init__(self, parent, depth, start, end, real_start, real_end):
        self.parent = parent
        self.children = dict()
        self.depth = depth
        self.start = start
        self.end = end
        self.printed = False
        self.real_start = real_start
        self.real_end = real_end

def create_new_leaf(node, s, suffix):
    leaf = SuffixTreeNode(node, len(s) - suffix, suffix + node.depth, len(s) - 1, suffix + node.depth, len(s) - 1)
    node.children[s[leaf.start]] = leaf
    return leaf

def break_edge(node, s, start, offset, suffix):
    start_char = s[start]
    mid_char = s[start+offset]
    print(f"start char = {start_char} and mid char = {mid_char}")
    print(f"depth would be {node.depth + offset} and start = {suffix} and end = {suffix + offset - 1}")
    mid_node = SuffixTreeNode(node, node.depth + offset, start, start + offset - 1, suffix, suffix + offset - 1)
    mid_node.children[mid_char] = node.children[start_char]
    node.children[start_char].parent = mid_node
    node.children[start_char].start += offset
    node.children[start_char].real_start += offset
    node.children[start_char] = mid_node
    return mid_node

def suffix_array_to_suffix_tree(order, lcp, s):
    root = SuffixTreeNode(None, 0, -1, -1, -1, -1)
    lcp_prev = 0
    cur = root
    for i in range(len(s)):
        suffix = order[i]
        print(f"starting suffix {s[suffix:]}")
        print(f"currently on node {s[cur.start:cur.end+1]}")
        while cur.depth > lcp_prev:
            cur = cur.parent
            start = order[i-1] + cur.depth
            print(f"climbing... on parent of {s[cur.children[s[start]].start:cur.children[s[start]].end+1]}")
        if cur.depth == lcp_prev:
            print('adding a new edge')
            cur = create_new_leaf(cur, s, suffix)
            print(s[cur.start:cur.end+1])
        else:
            start = order[i-1] + cur.depth
            offset = lcp_prev - cur.depth
            print(f"breaking the edge {s[cur.children[s[start]].start:cur.children[s[start]].end+1]}")
            print(f"while start is {cur.children[s[start]].start} and end is {cur.children[s[start]].end}")
            print(f"offset is {offset}")
            mid = break_edge(cur, s, start,  offset, suffix)
            print('adding a new edge')
            cur = create_new_leaf(mid, s, suffix)
            print(s[cur.start:cur.end+1])
        if i < len(s) - 1:
            lcp_prev = lcp[i]
        print()
    return root


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    sa = list(map(int, sys.stdin.readline().strip().split()))
    lcp = list(map(int, sys.stdin.readline().strip().split()))
    print(text)
    root = suffix_array_to_suffix_tree(sa, lcp, text)
    q = Queue()
    q.put(root)
    result_edges = []
    while not q.empty():
        node = q.get()
        if node.start != -1:
            result_edges.append((node.real_start, node.real_end+1))
        for edge in '$ACGT':
            if not edge in node.children:
                continue
            next_node = node.children[edge]
            q.put(next_node)
    for result in result_edges:
        print("%d %d" % (result[0], result[1]))
