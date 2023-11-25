# python3
import sys

def sort_suffixes(text):
    return list(map(str, sorted([i for i in range(len(text))], key=lambda x: text[x:])))

if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = sort_suffixes(text)
  print(" ".join(result))
