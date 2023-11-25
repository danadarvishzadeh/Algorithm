# python3
import sys


def make_tree(text):
    tree = [[(0, len(text), 0)]]
    l = len(text)
    for i in range(1, l):
        current = tree[0]
        j = i
        search_finished = 0
        while j < l and not search_finished:
            found = 0
            for k in range(len(current)):
                start, length, node_or_origin = current[k]
                edge = text[start:start+length]
                edge_index = 0
                while edge_index < length and j < l and edge[edge_index] == text[j]:
                    j += 1
                    edge_index += 1
                    found = 1
                if found and edge_index != length:
                    search_finished = 1
                    break
                if found and edge[-1] != '$':
                    current = tree[node_or_origin]
                    break
            if not found:
                break
        if found:
            tree.append([])
            current[k] = (start, edge_index, len(tree)-1)
            tree[-1].append((j, l-j, i))
            tree[-1].append((start+edge_index, length-edge_index, node_or_origin))
        elif j != i:
            current.append((i, l-j, i))
        else:
            current.append((i, l-i, i))
    return tree

def suffix(text):
    tree = make_tree(text)
    suffix_array = in_order(tree, text)
    return suffix_array

def is_leaf(node, text):
    start, length, _ = node
    if text[start+length-1] == '$':
        print('is leaf')
        return True
    return False

def print_tree(text):
    tree = make_tree(text)
    result = []
    for i in range(len(tree)):
        for start, length, _ in tree[i]:
            result.append(text[start:start+length])
    return result

def in_order(tree, text):
    stack = []
    suffix_array = []
    stack.append((0, len(tree[0])-1, 0))
    while stack:
        print(stack)
        node, max_, current = stack.pop()
        if is_leaf(tree[node][current], text):
            suffix_array.append(str(tree[node][current][-1]))
            if max_ > current:
                stack.append((node, max_, current+1))
        else:
            if max_ > current:
                stack.append((node, max_, current+1))
            stack.append((current, len(tree[current])-1, 0))
    return suffix_array

if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = suffix(text)
  print(" ".join(result))
  result = print_tree(text)
  print("\n".join(result))
