import sys
from math import comb

N, M, K = map(int, sys.stdin.readline().split())

num = 0
for k in range(K, M + 1):
    num += comb(M, k) * comb(N-M, M-k)

print(num / comb(N, M))