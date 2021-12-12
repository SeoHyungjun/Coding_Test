import sys

N, M = map(int, sys.stdin.readline().split())

print(min((N-1) + N*(M-1), (M-1) + M*(N-1)))