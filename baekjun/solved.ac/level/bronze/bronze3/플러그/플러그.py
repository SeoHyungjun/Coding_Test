import sys

N = int(sys.stdin.readline())
multitab = [int(sys.stdin.readline()) for _ in range(N)]
print(sum(multitab) - N + 1)