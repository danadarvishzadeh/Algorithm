import sys


def find(n, seq, number):
    r = n
    l = 0
    while l < r:
        mid = (r + l) // 2
        if seq[mid] == number:
            return mid
        elif seq[mid] < number:
            l = mid + 1
        else:
            r = mid
    return -1


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    seq = data[1:n+1]
    s = data[n+2:]
    for number in s:
        print(find(n, seq, number), end=' ' )
    print()
