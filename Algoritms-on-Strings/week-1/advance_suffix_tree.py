# python3
from queue import Queue
import sys


def make_tree(text):
    tree = {0: {(0, len(text)): 0}}
    #print(f"adding {text}")
    l = len(text)
    last_node = 0
    for i in range(1, l):
    #    print(f"processing {text[i:]}")
        #search for existing edge
        current = tree[0]
        j = i
        search_finished = 0
        while j < l and not search_finished:
            found = 0
            for (start, length), node_or_origin in current.items():
                edge = text[start:start+length]
    #            print(f"searching for {text[j:]} in {edge}")
                edge_index = 0
                while edge_index < length and j < l and edge[edge_index] == text[j]:
    #                print(f"found {text[j]} in {edge}")
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
    #        print(f"found in {text[start:start+length]}")
            last_node += 1
            tree[last_node] = {}
    #        print(f"breaking {text[start:start+length]}")
            del current[(start, length)]
    #        print('adding three edges')
    #        print(f"adding {text[start:start+edge_index]}")
            current[(start, edge_index)] = last_node
    #        print(f"adding {text[j:l]}")
            tree[last_node][(j, l-j)] = i
    #        print(f"adding {text[start+edge_index:start+length]}")
            tree[last_node][(start+edge_index, length-edge_index)] = node_or_origin
    #        print()
        elif j != i:
    #        print(f"adding {text[j:l]}")
    #        print(l-j)
            current[(j, l-j)] = i
    #        print()
        else:
    #        print(f"adding {text[i:l]}")
            current[(i, l-i)] = i
    #        print()
    return tree

def print_tree(text):
    tree = make_tree(text)
    result = []
    for node in tree.values():
        for (start, length) in node:
            result.append(text[start:start+length])
    #return sorted(result)
    return result

if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = print_tree(text)
  print("\n".join(result))
