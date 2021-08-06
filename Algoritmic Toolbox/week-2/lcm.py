a, b = map(int, input().split())
if a > b:
    a, b = b, a

for d in range(a, a * b + 1, a):
    if d % b == 0:
        print(d)
        break
