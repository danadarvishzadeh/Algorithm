import sys

class LCS:

    def __init__(self, s):
        self.s1 = s[0]
        self.s2 = s[1]
        self.changed = False
        if len(self.s1) < len(self.s2):
            self.s1, self.s2 = self.s2, self.s1
            self.changed = True
        self.p1 = 100003
        self.p2 = 100019
        self.x1 = 263
        self.x2 = 563

    def hash(self, string, x1, x2, p1, p2):
        h1 = h2 = 0
        for i in range(len(string)):
            h1 = (h1 * x1 + ord(string[i])) % p1
            h2 = (h2 * x2 + ord(string[i])) % p2
        return h1, h2

    def make_table(self, string, p1, p2, x1, x2, k):
        H1, H2 = [], []
        h1, h2 = self.hash(string[:k], x1, x2, p1, p2)
        H1.append(h1)
        H2.append(h2)
        y1 = pow(x1, k, p1)
        y2 = pow(x2, k, p2)
        for i in range(1, len(string)-k+1):
            h1 = (h1 * x1 + ord(string[i+k-1]) - y1 * ord(string[i-1])) % p1
            h2 = (h2 * x2 + ord(string[i+k-1]) - y2 * ord(string[i-1])) % p2
            H1.append(h1)
            H2.append(h2)
        return H1, H2

    def make_dict(self, string, p1 ,p2, x1, x2, k):
        D1 = {}
        D2 = {}
        d1, d2 = self.hash(string[:k], x1, x2, p1, p2)
        D1[d1] = 0
        D2[d2] = 0
        y1 = pow(x1, k, p1)
        y2 = pow(x2, k, p2)
        for i in range(1, len(string)-k+1):
            d1 = (d1 * x1 + ord(string[i+k-1]) - y1 * ord(string[i-1])) % p1
            d2 = (d2 * x2 + ord(string[i+k-1]) - y2 * ord(string[i-1])) % p2
            D1[d1] = i
            D2[d2] = i
        return D1, D2

    def search(self, table, dic):
        matches = dict()
        found = False
        for i in range(len(table)):
            tmp = dic.get(table[i], -1)
            if tmp != -1:
                matches[i] = tmp
                found = True
        return found, matches


    def solve(self):
        l = 1
        r = len(self.s2)
        a_, b_ = 0, 0
        length = 0
        while l < r:
            mid = (l + r) // 2
            H1, H2 = self.make_table(self.s1, self.p1, self.p2, self.x1, self.x2, mid)
            D1, D2 = self.make_dict(self.s2, self.p1, self.p2, self.x1, self.x2, mid)
            found1, matches1 = self.search(H1, D1)
            found2, matches2 = self.search(H2, D2)
            if found1 and found2:
                for a, b in matches1.items():
                    tmp = matches2.get(a, -1)
                    if tmp != -1:
                        length = mid
                        a_, b_ = a, b
                        l = mid + 1
                        break
                else:
                    r = mid
            else:
                r = mid 
        if self.changed:
            return b_, a_, length
        return a_, b_, length


def execute_queries(queries):
    results = []
    for q in queries:
        lcs = LCS(q.split())
        results.append(lcs.solve())
    for x in results:
        print(x[0], x[1], x[2], sep=' ')

if __name__ == "__main__":
    queries = sys.stdin.read().splitlines()
    execute_queries(queries)
