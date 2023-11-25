# python3
import sys

def make_trie(patterns):
    tree = dict()
    tree[0] = dict()
    last_node = 0
    for pattern in patterns:
        current = tree[0]
        for letter in pattern:
            exists = current.get(letter, 0)
            if exists:
                current = tree[exists]
            else:
                last_node += 1
                tree[last_node] = dict()
                current[letter] = last_node
                current = tree[last_node]
        current['null'] = 1
    return tree

def solve(text, patterns):
    result = []
    trie = make_trie(patterns)
    for i in range(len(text)):
        current = trie[0]
        symbol = i
        while True:
            if current.get('null', 0):
                result.append(i)
                break
            if symbol >= len(text):
                break
            exists = current.get(text[symbol], 0)
            if exists:
                current = trie[exists]
                symbol += 1
            else:
                break
    return result

text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
	patterns += [sys.stdin.readline().strip()]

ans = solve(text, patterns)

sys.stdout.write(' '.join(map(str, ans))+'\n')
