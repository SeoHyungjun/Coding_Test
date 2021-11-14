import sys
from itertools import combinations
from collections import defaultdict

N, S = map(int, sys.stdin.readline().split())
M = list(map(int, sys.stdin.readline().split()))

L = M[:N//2]
R = M[N//2:]

Lsum = defaultdict(int)
Rsum = defaultdict(int)
Lsum[0] = 1
Rsum[0] = 1

for i in range(1, len(L)+1):
    for com in combinations(L, i):
        Lsum[sum(com)] += 1

for i in range(1, len(R)+1):
    for com in combinations(R, i):
        Rsum[sum(com)] += 1

Lkey = sorted(Lsum.keys())
Rkey = sorted(Rsum.keys())

answer = 0
L = 0
R = len(Rkey)-1

while L < len(Lkey) and R >= 0:
    if Lkey[L] + Rkey[R] == S:
        answer += Lsum[Lkey[L]] * Rsum[Rkey[R]]
        L += 1
        R -= 1

    elif Lkey[L] + Rkey[R] > S:
        R -= 1

    else:
        L += 1

if S == 0:
    answer -= 1

print(answer)