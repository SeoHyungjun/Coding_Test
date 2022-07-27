import sys

def sum_of_number(word):
    result = 0

    for c in word:
        if c.isalpha():
            continue
        result += int(c)

    return result

N = int(sys.stdin.readline())
arr = [sys.stdin.readline().rstrip() for _ in range(N)]
arr.sort(key=lambda x:(len(x), sum_of_number(x), x))

print(*arr, sep = '\n')