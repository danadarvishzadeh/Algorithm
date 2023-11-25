#python3
import sys

def prep(transform, l):
    sorted_transform = sorted(transform)
    letters = {}
    first_occurance = []
    index = 0
    for i in range(l):
        if letters.get(sorted_transform[i], -1) < 0:
            first_occurance.append(i)
            letters[sorted_transform[i]] = index
            index += 1
    count = [[0 for _ in range(len(letters))]]
    for i in range(1, l+1):
        letter = letters[transform[i-1]]
        count.append([])
        for j in range(len(letters)):
            if letter != j:
                count[-1].append(count[-2][j])
            else:
                count[-1].append(count[-2][j]+1)
    return letters, first_occurance, count

def bwt(text, patterns):
    result = [str(0) for i in range(len(patterns))]
    patterns = [p[::-1] for p in patterns]
    l = len(text)
    letters, first_occurance, count = prep(text, l)
    for i in range(len(patterns)):
        top = 0
        bottom = l - 1
        pattern = patterns[i]
        lp = len(pattern)
        index = 0
        while top <= bottom:
            if index >= lp:
                result[i] = str(bottom-top+1)
                break
            letter = letters.get(pattern[index], -1)
            if letter == -1:
                break
            if count[bottom+1][letter] != 0:
                top = first_occurance[letter] + count[top][letter]
                bottom = first_occurance[letter] + count[bottom+1][letter] - 1
                index += 1
            else:
                break
    return result

if __name__ == "__main__":
    text = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    print(' '.join(bwt(text, patterns)))
