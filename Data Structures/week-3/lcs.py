import sys

def poly_hash(s, prime, multiplier):
    hash_value = 0
    for i in range(len(s) - 1, -1, -1):
        hash_value = (hash_value * multiplier + ord(s[i])) % prime
    return hash_value


def hash_table(s, p_len, prime, multiplier):
    H = list([] for _ in range(len(s) - p_len + 1))
    substring = s[len(s) - p_len:]
    H[len(s) - p_len] = poly_hash(substring, prime, multiplier)
    y = pow(multiplier, p_len, prime)
    for i in range(len(s) - p_len - 1, - 1, - 1):
        H[i] = (multiplier * H[i + 1] + ord(s[i]) - y * ord(s[i + p_len])) % prime
    return H


def hash_dict(s, p_len, prime, multiplier):
    D = {}
    substring = s[len(s) - p_len:]
    last = poly_hash(substring, prime, multiplier)
    D[last] = len(s) - p_len
    y = pow(multiplier, p_len, prime)
    for j in range(len(s) - p_len - 1, - 1, - 1):
        current = (multiplier * last + ord(s[j]) - y * ord(s[j + p_len])) % prime
        D[current] = j
        last = current
    return D


def search_substring(hash_table, hash_dict):
    check = False
    matches = {}
    for i in range(len(hash_table)):
        b_start = hash_dict.get(hash_table[i], -1)
        if b_start != -1:
            check = True
            matches[i] = b_start
    return check, matches


def max_length(string_a, string_b, low, high, length, aStart, bStart):
    mid = (low + high) // 2
    if low > high:
        return aStart, bStart, length
    prime1 = 1000000007
    prime2 = 1000004249
    x = 263
    aHash1 = hash_table(string_a, mid, prime1, x)
    aHash2 = hash_table(string_a, mid, prime2, x)
    bHash1 = hash_dict(string_b, mid, prime1, x)
    bHash2 = hash_dict(string_b, mid, prime2, x)
    check1, matches1 = search_substring(aHash1, bHash1)
    check2, matches2 = search_substring(aHash2, bHash2)
    if check1 and check2:
        for a, b in matches1.items():
            temp = matches2.get(a, -1)
            if temp != -1:
                length = mid
                aStart, bStart = a, b
                del aHash1, aHash2, bHash1, bHash2, matches1, matches2
                return max_length(string_a, string_b, mid + 1, high, length, aStart, bStart)
    return max_length(string_a, string_b, low, mid - 1, length, aStart, bStart)


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    for line in lines:
        s, t = line.split()
        k = min(len(s), len(t))
        if len(s) <= len(t):
            short_string, long_string = s, t
        else:
            short_string, long_string = t, s
        l, i, j = max_length(long_string, short_string, 0, k, 0, 0, 0)
        if len(s) <= len(t):
            print(i, l, j)
        else:
            print(l, i, j)
