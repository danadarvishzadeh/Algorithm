s, p = map(int, input().split())
points = []
for _ in range(s):
    seg = input().split()
    points.extend([(int(seg[0]), 'a'), (int(seg[1]), 'c')])
bets = list(map(int, input().split()))
points.extend(list(map(lambda x: (x, 'b'), bets)))

def merge(first, second):
    a, b = len(first), len(second)
    new = []
    while first and second:
        if first[0][0] < second[0][0]:
            new.append(first.pop(0))
        elif first[0][0] > second[0][0]:
            new.append(second.pop(0))
        else:
            x1, x2= first[0][1], second[0][1]
            if x1 < x2:
                new.append(first.pop(0))
            else:
                new.append(second.pop(0))
    if first:
        new.extend(first)
    if second:
        new.extend(second)
    return new

def merge_sort(points):
    l = len(points)
    if l == 1:
        return points
    first = merge_sort(points[:l//2])
    second = merge_sort(points[l//2:])
    return merge(first, second)

points = merge_sort(points)
point_seg_map = dict()
started = 0
for a, b in points:
    if b == 'a':
        started += 1
    elif b == 'b':
        point_seg_map[a] = started
    else:
        started -= 1

for i in bets:
    print(point_seg_map[i], end=' ')
print()
