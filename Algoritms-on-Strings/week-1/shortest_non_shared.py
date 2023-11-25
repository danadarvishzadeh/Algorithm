# python3
from queue import Queue
import sys


class SuffixTree:

    def __init__(self, p, q):
        self.text = p + '#' + q + '$'
        self.lt = len(self.text)
        self.lp = len(p)
        self.make_tree()
        #print(self.text)
        #for key, value in self.tree.items():
        #    print(key, value)
        #    print()

    def make_tree(self):
        self.tree = {0: {(0, self.lt): 0}}
        #print(f"adding {text}")
        last_node = 0
        for i in range(1, self.lt):
        #    print(f"processing {text[i:]}")
            #search for existing edge
            current = self.tree[0]
            j = i
            search_finished = 0
            while j < self.lt and not search_finished:
                found = 0
                for (start, length), node_or_origin in current.items():
                    edge = self.text[start:start+length]
        #            print(f"searching for {text[j:]} in {edge}")
                    edge_index = 0
                    while edge_index < length and j < self.lt and edge[edge_index] == self.text[j]:
        #                print(f"found {text[j]} in {edge}")
                        j += 1
                        edge_index += 1
                        found = 1
                    if found and edge_index != length:
                        search_finished = 1
                        break
                    if found and edge[-1] != '$':
                        current = self.tree[node_or_origin]
                        break
                if not found:
                    break
            if found:
        #        print(f"found in {text[start:start+length]}")
                last_node += 1
                self.tree[last_node] = {}
        #        print(f"breaking {text[start:start+length]}")
                del current[(start, length)]
        #        print('adding three edges')
        #        print(f"adding {text[start:start+edge_index]}")
                current[(start, edge_index)] = last_node
        #        print(f"adding {text[j:l]}")
                self.tree[last_node][(j, self.lt-j)] = i
        #        print(f"adding {text[start+edge_index:start+length]}")
                self.tree[last_node][(start+edge_index, length-edge_index)] = node_or_origin
        #        print()
            elif j != i:
        #        print(f"adding {text[j:l]}")
        #        print(l-j)
                current[(j, self.lt-j)] = i
        #        print()
            else:
        #        print(f"adding {text[i:l]}")
                current[(i, self.lt-i)] = i
        #        print()

    def is_leaf(self, start, length):
        return self.text[start+length-1].endswith('$')

    def type_l(self, length):
        return length > self.lp + 1

    def all_l(self, node):
        stack = []
        for item in self.tree[node].items():
            stack.append(item)
        while stack:
            (start, length), node = stack.pop()
            if self.is_leaf(start, length):
                if not self.type_l(length):
                    return False
            else:
                for item in self.tree[node].items():
                    stack.append(item)
        return True

    def print_tree(self):
        result = []
        stack = []
        for item in self.tree[0].items():
            stack.append(('', item))
        while stack:
            path, item = stack.pop()
            (start, length), node = item
            t = self.text[start:start+length]
            if self.is_leaf(start, length):
                if self.type_l(length):
                    if t.startswith('#'):
                        continue
                    else:
                        result.append(path+t[0])
            else:#is internal leaf
                if self.all_l(node):
                    result.append(path+t)
                else:
                    for new_item in self.tree[node].items():
                        stack.append((path+t, new_item))
        result.sort(key=lambda x: len(x))
        #print(result)
        return result[0]

def solve(p, q):
    tree = SuffixTree(p, q)
    result = tree.print_tree()
    return result

if __name__ == '__main__':
    p = sys.stdin.readline().strip()
    q = sys.stdin.readline().strip()
    ans = solve(p, q)
    sys.stdout.write(ans + '\n')
