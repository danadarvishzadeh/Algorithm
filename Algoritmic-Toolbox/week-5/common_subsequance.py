def find_lcs(A, B):
    ln_A = len(A)
    ln_B = len(B)
    D = list()
    for i in range(ln_B+1):
        D.append([0])
        if i == 0:
            D[i].extend([0 for _ in range(ln_A)])
    for i in range(1, ln_B+1):
        for j in range(1, ln_A+1):
            ins = D[i][j-1]
            dl = D[i-1][j]
            if int(A[j-1]) == int(B[i-1]):
                D[i].append(D[i-1][j-1] + 1)
            else:
            #    match = D[i-1][j-1]
                D[i].append(max(ins, dl))
    #[print(_) for _ in D]
    return D

def backtrack(D, A, B, i, j):
    seq = ''
    if i == 0 or j == 0:
        return seq
    if A[j-1] == B[i-1]:
        x = backtrack(D, A, B, i-1, j-1)
        if '-' in x:
            a = x.split('-')
            a = list(map(lambda z: seq + z + str(A[j-1]), a))
            seq = '-'.join(a)
        else:
            seq += x
            seq += str(A[j-1])
    elif D[i-1][j] > D[i][j-1]:
        x = backtrack(D, A, B, i-1, j)
        if '-' in x:
            a = x.split('-')
            a = list(map(lambda z: seq + z + A[j-1], a))
            seq = '-'.join(a)
        else:
            seq += x
    elif D[i-1][j] < D[i][j-1]:
        x = backtrack(D, A, B, i, j-1)
        if '-' in x:
            a = x.split('-')
            a = list(map(lambda z: seq + z + A[j-1], a))
            seq = '-'.join(a)
        else:
            seq += x
    else:
        x1 = backtrack(D, A, B, i, j-1)
        x2 = backtrack(D, A, B, i-1, j)
        seq = seq + x1 + '-' + seq + x2
    return seq

a = int(input())
A = list(map(int, input().split()))
b = int(input())
B = list(map(int, input().split()))
c = int(input())
C = list(map(int, input().split()))
D = find_lcs(A, B)
found = (backtrack(D, A, B, b, a)).split('-')
#print(found)
answer = list(map(lambda x: x[-1][-1], [ find_lcs(i, C) for i in found]))
#print(backtrack(D, found, C, c, len(found)))
print(max(answer))
