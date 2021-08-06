n, m = map(int, input().split())

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
n = (n+1) % pisano_p
m = (m+2) % pisano_p

to = fib(m)
from_ = fib(n)
print((to-from_)%10)
