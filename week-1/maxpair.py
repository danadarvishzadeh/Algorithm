_ = input()
given_array = list(map(int, input().split()))
given_array.sort()

print(given_array[-1] * given_array[-2])
