n = int(input())

MAX = 62
F = [0] * MAX
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        if F[n] == True:
            return F[n]
        k = (n+1)//2 if (n & 1) else n//2
        F[n] = (fib(k)**2 + fib(k-1)**2) if (n & 1) else ((2*fib(k-1) + fib(k))*fib(k))
        return F[n]

pisano_p = 60
n = n % pisano_p
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    current = fib(n+2)
    if current % 10 == 0:
        print(9)
    else:
        print((current-1) % 10)
