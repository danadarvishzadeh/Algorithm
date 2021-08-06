from random import shuffle
def backtrack(S, matrix, W, i):
    x = []
    while i > 0 and W > 0:
        if S[i-1] <= W and matrix[i-1][W] < matrix[i-1][W-S[i-1]] + S[i-1] and matrix[i-1][W] != matrix[i][W]:
            W -= S[i-1]
            x.append(S[i-1])
            S[i-1] = -1
            i -= 1
        else:
            i -= 1
    return list(filter(lambda x: True if x != -1 else False, S))

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

if __name__ == "__main__":

    n = int(input())
    S = list(map(int, input().split()))
    s = sum(S)
    if n < 3 or s % 3 != 0:
        print(0)
    else:
        W = s // 3
        if max(S) > W:
            print(0)
        else:
            if knap(S, W) and knap(S, W*2):
                print(1)
            else:
                print(0)
