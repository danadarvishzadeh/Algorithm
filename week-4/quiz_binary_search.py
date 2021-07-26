n = int(input())


def search(n):
    l = 0
    r = n
    numbers = [i for i in range(1, n+1)]
    i = 1
    while r - l > 1:
        mid = (r + l) // 2
        print('i=', i)
        print(numbers[mid])
        op = input()
        if op == 's':
            r = mid
        elif op == 'l':
            l = mid + 1
        elif op == 'ok':
            print('finished')
            break
        i += 1
    print('i=', i)
    print(numbers[l])

search(n)
