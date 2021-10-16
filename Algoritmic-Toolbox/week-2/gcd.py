a, b = map(int, input().split())
if a < b:
    a, b = b, a

while b > 1:
    if a % b == 0:
        break
    else:
        a, b = b, a%b
print(b)
