n = int(input())
if n == 1:
    print(1)
    print(1)
    quit()

W = n
candies = []
for i in range(1, n):
    if W > 2 * i:
        candies.append(i)
        W -= i
    else:
        candies.append(W)
        break

print(len(candies))
for _ in candies:
    print(_, end=' ')
print()
