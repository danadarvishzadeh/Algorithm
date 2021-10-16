import math


def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

def min_and_max(M, m, i, j, operators):
    min_ = math.inf
    max_ = -math.inf
    for k in range(i, j):
        op = operators[k]
        m1, m2, m3, m4 = M[i][k], M[k+1][j], m[i][k], m[k+1][j]
        a = calculate(m1, m2, op)
        b = calculate(m1, m4, op)
        c = calculate(m3, m2, op)
        d = calculate(m3, m4, op)
        min_ = min(min_, a, b, c, d)
        max_ = max(max_, a, b, c, d)
    return min_, max_

def placing_parentheses(S):
    operators = list()
    numbers = list()
    for i in S:
        if i in '-+*':
            operators.append(i)
        else:
            numbers.append(int(i))
    n = len(numbers)
    M = [[0 for i in range(n)]for j in range(n)]
    m = [[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        M[i][i] = numbers[i]
        m[i][i] = numbers[i]
    for s in range(1, n):
        for i in range(n-s):
            j = i + s
            m[i][j], M[i][j] = min_and_max(M, m, i, j, operators)
    return M[0][n-1]

if __name__ == "__main__":
    string = input()
    x = placing_parentheses(string)
    print(x)
