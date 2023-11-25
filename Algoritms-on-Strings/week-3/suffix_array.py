# python3
import sys
#sort partail sums of length 1
#create class array
#loop for l < |S|
#    do the sort doubled and class thing again
#return the order array

chars = {k: v for v, k in enumerate(('$', 'A', 'C', 'G', 'T'))}

def sort_characters(s):
    l = len(s)
    order = [0 for _ in range(l)]
    count = [0 for _ in range(5)]
    for i in range(l):
        count[chars[s[i]]] += 1
    for j in range(1, 5):
        count[j] += count[j-1]
    for i in range(l-1, -1, -1):
        c = chars[s[i]]
        count[c] -= 1
        order[count[c]] = i
    return order

def compute_char_classes(s, order):
    l = len(s)
    cls = [0 for _ in range(l)]
    for i in range(1, l):
        if s[order[i]] != s[order[i-1]]:
            cls[order[i]] = cls[order[i-1]] + 1
        else:
            cls[order[i]] = cls[order[i-1]]
    return cls

def doubled_sort(s, l, order, cls):
    size = len(s)
    count = [0 for _ in range(size)]
    new_order = [0 for _ in range(size)]
    for i in range(size):
        count[cls[i]] += 1
    for j in range(1, size):
        count[j] += count[j-1]
    for i in range(size-1, -1, -1):
        start = (order[i] - l + size) % size
        cl = cls[start]
        count[cl] -= 1
        new_order[count[cl]] = start
    return new_order

def update_classes(new_order, cls, l):
    n = len(new_order)
    new_cls = [0 for _ in range(n)]
    for i in range(1, n):
        cur = new_order[i]
        prev = new_order[i-1]
        mid = (cur + l) % n
        mid_prev = (prev + l) % n
        if cls[cur] != cls[prev] or cls[mid] != cls[mid_prev]:
            new_cls[cur] = new_cls[prev] + 1
        else:
            new_cls[cur] = new_cls[prev]
    return new_cls

def build_suffix_array(s):
    order = sort_characters(s)
    cls = compute_char_classes(s, order)
    l = 1
    while l < len(s):
        order = doubled_sort(s, l, order, cls)
        cls = update_classes(order, cls, l)
        l *= 2
    return order

if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
