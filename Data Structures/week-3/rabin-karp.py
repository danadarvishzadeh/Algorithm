
class Comparison:

    def __init__(self, p, t):
        self.p = p
        self.t = t
        self.prime = 500041
        self.x = 1
        self.H = [0 for i in range(len(t) - len(p) + 1)]
        self.result = []

    def hash(self, string):
        h = 0
        for i in range(len(string)-1, -1, -1):
            h = (h * self.x + ord(string[i])) % self.prime
        return h

    def prehash(self):
        l_p = len(self.p)
        l_t = len(self.t)
        y = 1
        for _ in range(l_p):
            y = (y * self.x) % self.prime
        self.H[l_t - l_p] = self.hash(self.t[l_t - l_p:])
        for i in range(l_t -l_p-1, -1, -1):
            h = (self.x * self.H[i+1] + ord(self.t[i]) - y * ord(self.t[i+l_p])) % self.prime
            self.H[i] = h

    def find_match(self):
        self.prehash()
        P = self.hash(self.p)
        for i in range(len(self.t) - len(self.p)+1):
            if self.H[i] == P and self.p == self.t[i:i+len(p)]:
                self.result.append(i)

    def prin(self):
        #print(self.result)
        for i in self.result:
            print(i, end=' ')
        print()


if __name__ == "__main__":
    p = input()
    t = input()
    c = Comparison(p, t)
    c.find_match()
    c.prin()
