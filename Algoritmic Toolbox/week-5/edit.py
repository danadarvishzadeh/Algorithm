def edit_distance(A, B):
    ln_A = len(A)
    ln_B = len(B)
    D = list()
    for i in range(ln_B+1):
        D.append([i])
        if i == 0:
            D[i].extend([_ for _ in range(1, ln_A+1)])
    for i in range(1, ln_B+1):
        for j in range(1, ln_A+1):
            ins = D[i][j-1] + 1
            dl = D[i-1][j] + 1
            if A[j-1] == B[i-1]:
                match = D[i-1][j-1]
            else:
                match = D[i-1][j-1] + 1
            D[i].append(min(ins, dl, match))
    return D[ln_B][ln_A]
    #return D
A = input()
B = input()
D = edit_distance(A, B)
print(D)
#[print(_) for _ in D]
