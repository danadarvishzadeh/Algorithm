def find_lcs(A, B, C, a, b, c):
    D = [[[0 for i in range(c+1)] for j in range(b+1)] for k in range(a+1)]
    for i in range(a+1):
        for j in range(b+1):
            for k in range(c+1):
                if i == 0 or j == 0 or k == 0:
                    D[i][j][k] = 0
                elif A[i-1] == B[j-1] == C[k-1]:
                    D[i][j][k] = D[i-1][j-1][k-1] + 1
                else:
                    D[i][j][k] = max(D[i-1][j][k], D[i][j-1][k], D[i][j][k-1])
    return(D[-1][-1][-1])


a = int(input())
A = input() 
b = int(input())
B = input()
c = int(input())
C = input() 

A, B, C = [int(i) for i in A.split()], [int(i) for i in B.split()],  [int(i) for i in C.split()]
print(find_lcs(A, B, C, a, b, c))
