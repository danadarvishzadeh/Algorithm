import sys

def ads(profits, slots):
    profits.sort()
    slots.sort()
    sum = 0
    for x, y in zip(profits, slots):
        sum += x * y
    return sum

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    profits = data[1:(n+1)]
    slots = data[(n+1):]
    print(ads(profits, slots))
