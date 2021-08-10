
class HashTable:

    def __init__(self):
        self.m = int(input())
        self.table = [[] for _ in range(self.m)]
        self.p = 1000000007
        self.x = 263
        self.alpha = 0
        self.size = 0

        
    def hash(self, string):
        h = 0
        for i in range(len(string)-1, -1, -1):
            h = (h * self.x + ord(string[i])) % self.p
        return h % self.m

    def load_check(self):
        return (self.size / self.m) < 0.5

    def rehash(self):
        if self.load_check():
            return
        pass
        

    def add(self , item):
        h = self.hash(item)
        if item in self.table[h]:
            return
        self.table[h].append(item)
        self.size += 1
        #self.rehash()

    def _del(self, item):
        h = self.hash(item)
        if not item in self.table[h]:
            return
        self.table[h].remove(item)

    def find(self, item):
        h = self.hash(item)
        if item in self.table[h]:
            print('yes')
        else:
            print('no')

    def check(self, i):
        table = self.table[i]
        if len(table):
            for item in reversed(self.table[i]):
                print(item, end=' ')
        print()

if __name__ == "__main__":
    dic = HashTable()
    n = int(input())
    queries = [input().split() for _ in range(n)]
    for q, f in queries:
        if q == 'add':
            dic.add(f)
        elif q == 'del':
            dic._del(f)
        elif q == 'check':
            dic.check(int(f))
        else:
            dic.find(f)
