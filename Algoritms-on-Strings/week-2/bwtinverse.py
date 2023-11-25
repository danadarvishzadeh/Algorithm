# python3

def prep(last):
    first = list(map(lambda x: x[1], sorted([(y, x) for x, y in enumerate(last)])))
    last_to_first = [0 for _ in range(len(last))]
    for i in range(len(last)):
        last_to_first[first[i]] = i
    return last_to_first

def bwtinverse(transform):
    last_to_first = prep(transform)
    index = 0
    string = '$'
    while transform[index] != '$':
        string += transform[index]
        index = last_to_first[index]
    return string[::-1]

if __name__ == "__main__":
    transform = input()
    print(bwtinverse(transform))
