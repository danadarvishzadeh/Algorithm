import sys

def merge(first, second):
    new = []
    inversion = 0
    a, b = len(first), len(second)
    if a > 1:
        *first, i = first
        inversion += i
    if b > 1:
        *second, i = second
        inversion += i
    while first and second:
        if first[0] <= second[0]:
            new.append(first.pop(0))
        elif first[0] > second[0]:
            new.append(second.pop(0))
            #inversion += 1
            inversion += len(first)
    if first:
        #inversion += (len(first) - 1) * len(new)
        new.extend(first)
    elif second:
        new.extend(second)
    new.append(inversion)
    return new


def merge_sort(A):
    l = len(A)
    if l == 1:
        return A
    first = merge_sort(A[:l//2])
    second = merge_sort(A[l//2:])
    return merge(first, second)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    _, *data = data
    *_, I = merge_sort(data)
    print(I)
