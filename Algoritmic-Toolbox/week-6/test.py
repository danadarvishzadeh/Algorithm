import numpy

def partition(W, n, S):
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
        print('0')
    else:
        print('1')

if __name__ == '__main__':
    n = int(input())
    item_weights = [int(i) for i in input().split()]
    total_weight = sum(item_weights)
    if n < 3: 
        print('0')
    elif total_weight % 3 != 0: 
        print('0')
    else:
        partition(total_weight // 3, n, item_weights)
