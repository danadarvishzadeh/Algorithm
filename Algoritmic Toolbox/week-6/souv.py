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

def knap(S):
    s_sum = sum(S)
    if s_sum % 3 != 0 or len(S) < 3:
        return 0
    W = s_sum // 3
    shuffle(S)
    for _ in range(2):
        ln_s = len(S)
        matrix = [[0 for i in range(W+1)]for j in range(ln_s+1)]
        for w in range(1, W+1):
            for i in range(1, ln_s+1):
                matrix[i][w] = matrix[i-1][w]
                if S[i-1] <= w:
                    mat = matrix[i-1][w-S[i-1]] + S[i-1]
                    matrix[i][w] = max(mat, matrix[i][w])
        if matrix[-1][-1] != W:
            return 0
        S = backtrack(S, matrix, W, ln_s)
    if sum(S) == W:
        return 1
    return 0

if __name__ == "__main__":

    _ = input()
    S = list(map(int, input().split()))
    a = knap(S)
    b = knap(S)
    print(a or b)
