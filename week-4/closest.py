import math

def compute_d(A, B):
    return math.sqrt((A[0]-B[0])**2+(A[1]-B[1])**2)

def brute(A):
    d = compute_d(A[0], A[1])
    l = len(A)
    if l == 2:
        return d
    for i in range(l-1):
        for j in range(i+1, l):
            if i != 0 and j != 1:
                c = compute_d(A[i], A[j])
                if c < d:
                    d = c
    return d

def check_distance_split(ax, ay, d):
    l = len(ax)
    mid = ax[l//2][0]
    sy = [x for x in ay if mid - d <= x[0] <= mid + d]
    l = len(sy)
    for i in range(l-1):
        for j in range(i+1, min(i+5, l)):
            c = compute_d(sy[i], sy[j])
            if c < d:
                d = c
    return d

def check_distance(ax, ay):
    l = len(ax)
    if l <= 3:
        return brute(ax)
    mid = l//2
    Qx = ax[:mid]
    Rx = ax[mid:]
    
    midpoint = ax[mid][0]
    Qy = list()
    Ry = list()
    for x in ay:
        if x[0] < midpoint:
            Qy.append(x)
        else:
            Ry.append(x)
    d1 = check_distance(Qx, Qy)
    d2 = check_distance(Rx, Ry)
    d = min(d1, d2)
    d = check_distance_split(ax, ay, d)
    return d

def main():

    n = int(input())
    S = [list(map(int, input().split())) for _ in range(n)]
    ax = sorted(S)
    ay = sorted(S, key=lambda x: (x[1], [0]))
    d = check_distance(ax, ay)
    print("{:.20f}".format(d))
        

if __name__ == "__main__":
    main()
