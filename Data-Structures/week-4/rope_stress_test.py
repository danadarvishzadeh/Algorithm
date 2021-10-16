from splay_tree import create_tree, solve
from random import randint, randrange, choice
from string import ascii_lowercase as alc

def generate():
    n = randint(2, 15)
    s = ''.join([choice(alc) for _ in range(n)])
    q = randint(1, 100000)
    queries = []
    for _ in range(q):
        i = randrange(n-1)
        j = randint(i, n-1)
        k = randrange(n-(j-1+1))
        queries.append((i, j, k))
    return s, q, queries[:-1]


def naive_solve(string, i, j, k):
    moving = string[i:j+1]
    remain = string[:i] + string[j+1:]
    return remain[:k] + moving + remain[k:]

def main():
    while True:
        string, _, queries = generate()
        tree = create_tree(string)
        print('----start----')
        print(f'string={string}')
        print(f'tree={tree.order()}')
        print('-------------')
        for i, j, k in queries:
            tmp = naive_solve(string, i, j, k)
            tree = solve(tree, i, j, k)
            print(f'\nstring={string}')
            print(f'tmp   ={tmp}')
            print(f'tree  ={tree.order()}')
            print(f'i={i} j={j} k={k}')
            if tmp != tree.order():
                exit()
            else:
                string = tmp

if __name__ == "__main__":
    main()
