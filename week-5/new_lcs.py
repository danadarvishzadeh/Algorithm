def lcsOf3(X, Y, Z, m, n, o):
    L = [[[0 for i in range(o+1)] for j in range(n+1)]for k in range(m+1)]
 #   L = [[[0]*(o+1)]*(n+1)]*(m+1)
    for i in range(m+1):
        for j in range(n+1):
            for k in range(o+1):
                if (i == 0 or j == 0 or k == 0):
                    L[i][j][k] = 0
                elif (X[i-1] == Y[j-1] and X[i-1] == Z[k-1]):
                    L[i][j][k] = L[i-1][j-1][k-1] + 1
                else:
                    L[i][j][k] = max(max(L[i-1][j][k], L[i][j-1][k]),L[i][j][k-1])
    [print(i) for i in L]
    return L[m][n][o]

X = '8 3 2 1 7'.split()
Y = '8 2 1 3 8 10 7'.split()
Z = '6 8 3 1 4 7'.split()

X, Y, Z = [int(i) for i in X], [int(i) for i in Y], [int(i) for i in Z]

m = len(X)
n = len(Y)
o = len(Z)

print('Length of LCS is', lcsOf3(X, Y, Z, m, n, o))
