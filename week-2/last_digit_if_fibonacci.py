n = int(input())

x1 = 0
x2 = 1
if n == 0:
    print(x1)
elif n == 1:
    print(x2)
else:
    for i in range(1, n):
        x1, x2 = x2, (x1+x2) % 10

    print(x2)

