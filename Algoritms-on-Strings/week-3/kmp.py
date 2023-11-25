# python3
import sys

def compute_prefix(text):
    prefixes = [0]
    border = 0
    for i in range(1, len(text)):
        while border > 0 and text[i] != text[border]:
            border = prefixes[border-1]
        if text[i] == text[border]:
            border += 1
        else:
            border = 0
        prefixes.append(border)
    return prefixes

def find_pattern(pattern, text):
    """
    Find all the occurrences of the pattern in the text
    and return a list of all positions in the text
    where the pattern starts in the text.
    """
    result = []
    combined_text = pattern + '$' + text
    lp = len(pattern)
    prefixes = compute_prefix(combined_text)
    for i in range(lp+1, len(combined_text)):
        if prefixes[i] == lp:
            result.append(i - 2 * lp)
    return result


if __name__ == '__main__':
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))

