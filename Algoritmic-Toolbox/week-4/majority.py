_ = int(input())

digits = list(map(int, input().split()))


def merge(f, s, digits):
    if f == -1 and s == -1:
        return -1
    elif f == s:
        return f
    elif f > 0 or s > 0:
        fm = 0
        sm = 0
        l = len(digits)
        for i in digits:
            if i == f:
                fm += 1
            elif i == s:
                sm += 1
        if fm > sm and fm > l//2:
            return f
        elif fm < sm and sm > l//2:
            return s
        else:
            return -1


def maj(digits):
    l = len(digits)
    if l == 1:
        return digits[0]
    f = maj(digits[l//2:])
    s = maj(digits[:l//2])
    return merge(f, s, digits)

a = maj(digits)
if a == -1:
    print(0)
else:
    print(1)
