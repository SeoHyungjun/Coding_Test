import sys

N = int(sys.stdin.readline())
for _ in range(N):
    word = sys.stdin.readline().rstrip()

    if len(word) > 10:
        print(word[0] + str(len(word[1:-1])) + word[-1])
    else:
        print(word)