import sys

N, M, K = map(int, sys.stdin.readline().split())
print(min(M, K) + N - max(M, K))