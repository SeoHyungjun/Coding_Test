# 17:30 -> 17:38

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())

    max_sum = [0] * N

    for i in range(N):
        A, B, C = map(int, sys.stdin.readline().split())
        max_day = max(A,B,C)
        max_sum[i] = max_day if max_day >= 0 else 0

    print(sum(max_sum))