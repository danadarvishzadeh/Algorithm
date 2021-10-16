import sys

class Equalizer:

    def __init__(self, t, p):
        self.t = t
        self.p = p
        self.T1 = [0]
        self.T2 = [0]
        self.P1 = [0]
        self.P2 = [0]
        self.x1 = 2
        self.x2 = 3
        self.m1 = 200003
        self.m2 = 200017

    def prehash1(self):
        l = len(self.t)
        for i in range(l):
            t1 = (self.T1[-1] * self.x1 + ord(self.t[i])) % self.m1
            t2 = (self.T2[-1] * self.x2 + ord(self.t[i])) % self.m2
            self.T1.append(t1)
            self.T2.append(t2)

    def prehash2(self):
        l = len(self.p)
        for i in range(l):
            p1 = (self.P1[-1] * self.x1 + ord(self.p[i])) % self.m1
            p2 = (self.P2[-1] * self.x2 + ord(self.p[i])) % self.m2
            self.P1.append(p1)
            self.P2.append(p2)

    def prehash(self):
        self.prehash1()
        self.prehash2()
        self.prey()

    def prey(self):
        self.y1 = [1]
        self.y2 = [1]
        for i in range(1, len(self.p)+1):
            self.y1.append((self.y1[-1] * self.x1)%self.m1)
            self.y2.append((self.y2[-1] * self.x2)%self.m2)

    def are_equal(self, i, j, l):
        a, b, d = i, j, l
        y1 = self.y1[d]
        y2 = self.y2[d]
        td1 = (self.T1[a+d] - y1 * self.T1[a]) % self.m1
        td2 = (self.T2[a+d] - y2 * self.T2[a]) % self.m2
        pd1 = (self.P1[b+d] - y1 * self.P1[b]) % self.m1
        pd2 = (self.P2[b+d] - y2 * self.P2[b]) % self.m2
        if td1 == pd1 and td2 == pd2:
            return True
        return False


def count_mismatches(i, low, high, t, p, TP, k):
    if k < 0:
        return False, k
    if low >= high:
        if t[i+high] == p[high]:
            return bool(k-1>=0), k - 1
    mid = (low + high) // 2
    if t[i+mid] != p[mid]:
        k -= 1
    if k < 0:
        return False, k
    if not TP.are_equal(i+low, low, mid-low):
        if k > 0:
            b, z = count_mismatches(i, low, mid-1, t, p, TP, k)
            if b:
                k = z
            else:
                return False, z
        else:
            return False, k
    if not TP.are_equal(i+mid+1, mid+1, high-mid):
        if k > 0:
            b, z = count_mismatches(i, mid+1, high, t, p, TP, k)
            if b:
                k = z
            else:
                return False, z
        else:
            return False, k
    return True, k


def solve(t, p, k):
    res = []
    l = len(p)
    if l > len(t):
        return res
    TP = Equalizer(t, p)
    TP.prehash()
    for i in range(len(t)-l+1):
        b, _ = count_mismatches(i, 0, l-1, t, p, TP, k)
        if b:
            res.append(i)
    return res


prime = 200003
x = 3

if __name__ == "__main__":
    data = sys.stdin.read().splitlines()
    for line in data:
        line = line.split()
        res = solve(line[1], line[2], int(line[0]))
        print(len(res), end=' ')
        for i in res:
            print(i, end=' ')
        print()
