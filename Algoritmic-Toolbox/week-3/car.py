import sys

def car(cap, n, stations):
    tank = cap
    mins = 0
    for s in range(n+1):
        #print('station', stations[s])
        #print('next station', stations[s+1])
        dist = stations[s+1] - stations[s]
        #print('tank:', tank)
        #print('distance', dist)
        if tank >= dist:
            tank -= dist
        #    print('tank:', tank, end='\n\n')
        elif tank < dist <= cap:
            tank = cap - dist
            mins += 1
        #    print('tank:', tank, end='\n\n')
        else:
            return(-1)
    if mins > n:
        return(-1)
    return(mins)
            
if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    cap = data[1]
    n = data[2]
    stations = [0] + data[3:] + data[:1]
    print(car(cap, n, stations))
