n = int(input())
a = [i for i in range(1, n+1)]
b = [0, 1]
x1 = 0
x2 = 1
if n == 0:
    print(x1)
elif n == 1:
    print(x2)
else:
    for i in range(1, n):
        x1, x2 = x2, x1+x2
        b.append(x2)

print(a, b)
