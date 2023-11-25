# python3
import sys

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

def pattern_matching(pattern, suffix_array, text, size):
    min_index = 0
    max_index = size
    pattern_size = len(pattern)
    while min_index < max_index:
        mid_index = (min_index + max_index) // 2
        suffix_start = suffix_array[mid_index]
        if pattern > text[suffix_start:suffix_start+pattern_size]:
            min_index = mid_index + 1
        else:
            max_index = mid_index
    start = min_index
    max_index = size
    while min_index < max_index:
        mid_index = (min_index + max_index) // 2
        suffix_start = suffix_array[mid_index]
        if pattern < text[suffix_start:suffix_start+pattern_size]:
            max_index = mid_index
        else:
            min_index = mid_index + 1
    end = max_index
    if start > end:
        return []
    else:
        return suffix_array[start:end]

def find_occurrences(text, patterns):
    occs = set()
    text += '$'
    suffix_array = build_suffix_array(text)
    size = len(text)
    for p in patterns:
        for result in pattern_matching(p, suffix_array, text, size):
            occs.add(result)
    return occs

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    occs = find_occurrences(text, patterns)
    print(" ".join(map(str, occs)))
