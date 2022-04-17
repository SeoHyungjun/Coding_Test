import sys

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break

    words = [sys.stdin.readline().rstrip() for _ in range(N)]

    words.sort(key = lambda x : x.lower())
    print(words[0])