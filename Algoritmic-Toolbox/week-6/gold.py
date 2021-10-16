def knapsack(W, golds):
    value = [[0 for i in range(W+1)] for j in range(len(golds)+1)]
    for w in range(W+1):
        for i in range(len(golds)+1):
            if w == 0 or i == 0:
                value[i][w] = 0
            else:
                value[i][w] = value[i-1][w]
                if golds[i-1] <= w:
                    val = value[i-1][w-golds[i-1]] + golds[i-1]
                    value[i][w] = max(val, value[i][w])
    return value[-1][-1], value


def backtrack(S, matrix, W, i):
    x = []
    [print(_) for _ in matrix]
    while i > 0 and W > 0:
        print('--', W, i)
        if matrix[i-1][W] < matrix[i-1][W-S[i-1]] + S[i-1] and matrix[i-1][W] != matrix[i][W] and S[i-1] <= W:
            x.append(S[i-1])
            W -= S[i-1]
            i -= 1
        else:
            i -= 1
    #return list(filter(lambda x: True if x != 0 else False, S))
    return ' '.join(list(map(str, x)))

W, _ = map(int, input().split())
golds = list(map(int, input().split()))
val, value = knapsack(W, golds)
print(val)
D = backtrack(golds, value, W, len(golds))
print(D)
