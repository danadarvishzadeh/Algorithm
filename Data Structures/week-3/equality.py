
class Equalizer:

    def __init__(self, s):
        self.s = s
        self.H1 = [0]
        self.H2 = [0]
        self.x1 = 2
        self.x2 = 3
        self.m1 = 500029
        self.m2 = 500041

    def prehash(self):
        l = len(self.s)
        for i in range(l):
            h1 = (self.H1[-1] * self.x1 + ord(self.s[i])) % self.m1
            h2 = (self.H2[-1] * self.x2 + ord(self.s[i])) % self.m2
            self.H1.append(h1)
            self.H2.append(h2)

    def answer(self, args):
        a, b, d = args
        y1 = pow(self.x1, d, self.m1)
        y2 = pow(self.x2, d, self.m2)
        ad1 = (self.H1[a+d] - y1 * self.H1[a]) % self.m1
        ad2 = (self.H2[a+d] - y2 * self.H2[a]) % self.m2
        bd1 = (self.H1[b+d] - y1 * self.H1[b]) % self.m1
        bd2 = (self.H2[b+d] - y2 * self.H2[b]) % self.m2
        if ad1 == bd1 and ad2 == bd2:
            return 'Yes'
        return 'No'


if __name__ == "__main__":
    e = Equalizer(input())
    e.prehash()
    n = int(input())
    results = []
    for _ in range(n):
        results.append(e.answer(map(int, input().split())))
    for line in results:
        print(line)
