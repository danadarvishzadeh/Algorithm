n = int(input())
digits = list(map(int, input().split()))

def is_greater_or_equal(digit, mx):
    digit, mx = str(digit), str(mx)
    while True:
        a, b = len(digit), len(mx)
        for i in range(min(a, b)):
            if digit[i] > mx[i]:
                return True
            elif digit[i] < mx[i]:
                return False
        if abs(a-b) > 0:
            if a < b:
                mx = mx[min(a, b):]
            elif a > b:
                digit = digit[min(a, b):]
        else:
            return True

result = ''
while len(digits) > 0:
    mx = 0
    for digit in digits:
        if is_greater_or_equal(digit, mx):
            mx = digit
    result += str(mx)
    digits.remove(mx)
print(result)
