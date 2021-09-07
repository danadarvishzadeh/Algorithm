from avl_tree_2 import AVL
from random import randint, randrange, choice

def generate():
    n = randrange(1000000)
    q = [n]
    limit = randint(1, 10000000000)
    ops = '+-?s'
    for _ in range(n):
        rand_op = choice(ops)
        if rand_op == 's':
            l = randrange(limit)
            r = randint(l, limit)
            q.append(' '.join((rand_op, str(l), str(r))))
        else:
            l = randrange(limit)
            q.append(' '.join((rand_op, str(l))))
    return q

def interface():
    i = input()
    while i != 'q':
        exec(i)
        i = input()

def main():
    while True:
        t = []
        n, *query = generate()
        M = 1000000001
        print(n)
        for q in query:
            [print(_, end=' ') for _ in q]
            print()
        print(f"new query: {query}", end='\n\n')
        x = 0
        summ = 0
        answer = []
        tree = AVL()
        for i in query:
            q = i.split()
            print(q)
            print()
            if q[0] == '+':
                tree.insert((int(q[1]) + x) % M)
                try:
                    t.index((int(q[1])+ summ) % M )
                except:
                    t.append((int(q[1]) + summ) % M)
                    t.sort()
            elif q[0] == '-':
                if tree.find((int(q[1])+ x) % M):
                    try:
                        t.remove((int(q[1]) + summ) % M)
                    except:
                        print('exited on delete')
                        tree.order()
                        print(t)
                        exit()
                tree.delete((int(q[1]) + x) % M)
            elif q[0] == '?':
                ans = tree.find((int(q[1]) + x) % M)
                try:
                    t.index((int(q[1]) + summ) % M)
                except:
                    if ans:
                        print('exited of search')
                        quit()
            else:
                x = tree.rsum((int(q[1]) + x) % M, (int(q[2]) + x) % M)
                print(x)
                l = ((int(q[1]) + summ) % M)
                r = ((int(q[2]) + summ) % M)
                summ = 0
                for h in t:
                    if l <= h <= r:
                        summ += h
                print(summ)
                if x != summ:
                    print('tree order:')
                    tree.order()
                    print(f"list: {t}")
                    quit()
            with open('q.txt', 'w') as f:
                f.write('\n'.join(query))

if __name__ == "__main__":
    main()
