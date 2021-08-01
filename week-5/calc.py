def calculator(number):
    min_num_ops = [0, 0]
    for i in range(2, number+1):
        min_num_ops.append(min_num_ops[-1]+1)
        if i % 3 == 0:
            min_num_ops[i] = min(min_num_ops[i//3]+1, min_num_ops[i])
        if i % 2 == 0:
            min_num_ops[i] = min(min_num_ops[i//2]+1, min_num_ops[i])
    return min_num_ops

def backtrack(D, number):
    if number <= 1:
        print(1, end=' ')
        return
    elif D[number] == D[number//3] + 1:
        backtrack(D, number//3)
        print(number, end=' ')
    elif D[number] == D[number//2] + 1:
        backtrack(D, number//2)
        print(number, end=' ')
    else:
        backtrack(D, number-1)
        print(number, end=' ')

number = int(input())
D = calculator(number)
print(D[-1])
backtrack(D, number)
print()
