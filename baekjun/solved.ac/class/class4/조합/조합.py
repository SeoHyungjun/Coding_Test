import sys
from math import factorial

N, M = map(int, sys.stdin.readline().split())

answer = 1

for i in range(M):
    answer *= N-i
    answer //= i+1

print(answer)