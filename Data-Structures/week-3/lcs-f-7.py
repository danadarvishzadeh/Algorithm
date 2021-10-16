import sys

class LCS:

    def __init__(self, s):
        self.s1 = s[0]
        self.s2 = s[1]
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
        for i in range(1, len(string)-k+1):
            h1 = (h1 * x1 + ord(string[i+k-1]) - pow(x1, k, p1) * ord(string[i-1])) % p1
            h2 = (h2 * x2 + ord(string[i+k-1]) - pow(x2, k, p2) * ord(string[i-1])) % p2
            H1.append(h1)
            H2.append(h2)
        return H1, H2

    def solve(self):
        l = 1
        r = min(len(self.s1), len(self.s2))
        result = (0, 0)
        length = 0
        while l <= r:
            mid = (l + r) // 2
            H1, H2 = self.make_table(self.s1, self.p1, self.p2, self.x1, self.x2, mid)
            h1, h2 = self.make_table(self.s2, self.p1, self.p2, self.x1, self.x2, mid)
            for i, j in zip(h1, h2):
                if i in H1 and j in H2:
                    result = (H1.index(i), h1.index(i))
                    length = mid
                    l = mid + 1
            else:
                r = mid -1
        return result, length


def execute_queries(queries):
    results = []
    for q in queries:
        lcs = LCS(q.split())
        results.append(lcs.solve())
    for x in results:
        print(x[0][0], x[0][1], x[1], sep=' ')

if __name__ == "__main__":
    queries = sys.stdin.read().splitlines()
    execute_queries(queries)
