import random
from random import shuffle
import sys, itertools
import numpy


def partition(n, S):
    if sum(S) % 3 != 0:
        return 0
    W = sum(S) // 3
    cnt = 0
    value = numpy.zeros((W+1, n+1))
    for i in range(1, W+1):
        for j in range(1, n+1):
            value[i][j] = value[i][j-1]
            if S[j-1]<=i:
                temp = value[i-S[j-1]][j-1] + S[j-1]
                if temp > value[i][j]:
                    value[i][j] = temp
            if value[i][j] == W:
                cnt += 1
    print(value)
    if cnt < 3:
        return 0
    else:
        return 1

def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)
        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1
    return 0

def knap(S, W):
    #shuffle(S)
    ln_s = len(S)
    matrix = [[0 for i in range(W+1)]for j in range(ln_s+1)]
    for w in range(1, W+1):
        for i in range(1, ln_s+1):
            matrix[i][w] = matrix[i-1][w]
            if S[i-1] <= w:
                mat = matrix[i-1][w-S[i-1]] + S[i-1]
                matrix[i][w] = max(mat, matrix[i][w])
    return matrix[-1][-1] == W

def r(n, S):
    s = sum(S)
    if n < 3 or s % 3 != 0:
        return 0
    else:
        W = s // 3
        for i in S:
            if i > W:
                return 0
        if knap(S, W) and knap(S, W*2):
            return 1
        else:
            return 0


if __name__ == "__main__":
    x, y = map(int, input().split())
    while True:
        print('**************')
        n = random.randint(3, x)
        vi = [random.randrange(y) for _ in range(n)]
        print(vi)
        b = partition3(vi)
        a = r(n, vi)
        if a != b:
            print('answer:', a)
            print('naive:', b)
            exit()
        else:
            print('answer:', a, 'naive:', b, sep=' ')
