n = int(input())
seg = []
crosses = []
for _ in range(n):
    a, b = map(int, input().split())
    seg.append([a, b])
seg.sort()
i = 0
while i < n:
    included_segments = 1
    end = seg[i][1]
    for j in range(i+1, n):
        if seg[j][0] <= end:
            included_segments += 1
            if seg[j][1] < end:
                end = seg[j][1]
        else:
            break
    crosses.append(end)
    i += included_segments

print(len(crosses))
for _ in crosses:
    print(_, end=' ')
print()
