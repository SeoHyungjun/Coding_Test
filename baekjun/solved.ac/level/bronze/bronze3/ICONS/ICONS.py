import sys
import math

N = int(sys.stdin.readline())

min_sum = N+1
a, b = N, 1
for i in range(1, N+1):
    for j in range(1, N+1):
        if i + j < min_sum and N <= i*j:
            min_sum = i + j
            a, b = i, j

print(a, b)