import sys
import math

N, M = map(int, sys.stdin.readline().split())

min_set, min_one = 1001, 1001
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    min_set = min(min_set, a)
    min_one = min(min_one, b)

print(min(math.ceil(N / 6) * min_set, N // 6 * min_set + N % 6 * min_one, min_one * N))