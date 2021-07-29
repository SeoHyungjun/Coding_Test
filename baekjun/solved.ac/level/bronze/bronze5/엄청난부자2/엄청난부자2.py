import sys

N, M = map(int, sys.stdin.readline().split())
print(*divmod(N, M), sep = '\n')