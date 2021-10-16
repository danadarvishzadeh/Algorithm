from random import randint, randrange, choice
from splay_tree import SPlay as ss

def main():
    while True:
        i = randint(1, 1000)
        s1 = ss()
        s2 = set()
        print()
        for _ in range(i):
            x = randrange(5000)
            op = choice(['i', 'd'])
            A = s1.order()
            print(f"x={x} op={op}")
            if op == 'i':
                s1.insert(x, x)
                s2.add(x)
            else:
                c1 = x in A
                c2 = x in s2
                if c1 and c2:
                    s1.delete(x)
                    s2.remove(x)
                elif c1 != c2:
                    print('on delete')
                    print(x)
                    print(A)
                    print(list(s2))
                    exit()
        if s1.order() != sorted(list(s2)):
            print('at the end')
            print('s1:', s1.order())
            print('s2:', sorted(list(s2)))
            exit()


if __name__ == "__main__":
    main()
