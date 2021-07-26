n, m = map(int, input().split())

def pisano_period(m):

    previous = 0
    current = 1
    for i in range(m*m):
        previous, current = current, (current+previous)%m
        if previous == 0 and current == 1:
            return i + 1

pisano_p = pisano_period(m)
n = n % pisano_p
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    previous, current =  0, 1
    for i in range(1, n):
        previous, current = current, current+previous
    print(current % m)
