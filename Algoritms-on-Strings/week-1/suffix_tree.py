# python3
from queue import Queue
import sys


def make_tree(text):
    tree = dict()
    tree[0] = dict()
    last_node = 0
    for i in range(len(text)):
        current = tree[0]
        for letter in text[i:]:
            exists = current.get(letter, 0)
            if exists:
                current = tree[exists]
            elif letter == '$':
                current[letter] = i
            else:
                last_node += 1
                tree[last_node] = dict()
                current[letter] = last_node
                current = tree[last_node]
    return tree

def compress(edge, next_node, before_dict, tree):
    next_dict = tree[next_node]
    next_edge = list(next_dict.keys())[0]
    next_value = list(next_dict.values())[0]
    before_dict[edge + next_edge] = next_value
    if next_edge != '$':
        del tree[next_node]
    del before_dict[edge]
    return edge + next_edge, next_value

def compress_tree(tree):
    q = Queue()
    q.put(0)
    while not q.empty():
        before_node = q.get()
        before_dict = tree[before_node]
        items = list(before_dict.items())
        for edge, next_node in items:
            x = next_node
            while edge[-1] != '$' and len(tree[next_node]) <= 1:
                edge, next_node = compress(edge, next_node, before_dict, tree)
            if edge[-1] != '$':
                q.put(next_node)

#def print_tree(text):
#    """
#    Build a suffix tree of the string text and return a list
#    with all of the labels of its edges (the corresponding 
#    substrings of the text) in any order.
#    """
#    tree = make_tree(text)
#    compress(tree)
#    result = []
#    stack = [(0, '', 0, len(tree[0]))]
#    while stack:
#        node, string, visited, max_ = stack.pop()
#        if visited == max_:
#            continue
#        for key, value in tree[node].items():
#            if key == '$':
#                result.append(string+'$')
#            else:
#                stack.append((value, string+key, 0, len(tree[value])))
#    return result
#

def print_tree(text):
    tree = make_tree(text)
    compress_tree(tree)
    #print(tree)
    result = []
    q = Queue()
    q.put(0)
    while not q.empty():
        new = q.get()
        for key, value in tree[new].items():
            result.append(key)
            if key[-1] != '$':
                q.put(value)
    return result
    #return ['', '', '']

if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = print_tree(text)
  print("\n".join(result))
  #print(make_tree(text))
