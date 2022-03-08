import sys
from bisect import bisect_right

def find_score(t):
    return bisect_right(score, t)

N, Q = map(int, sys.stdin.readline().split())

score = [int(sys.stdin.readline()) for _ in range(N)]
for i in range(1, N):
    score[i] += score[i-1]

for _ in range(Q):
    t = int(sys.stdin.readline())

    print(find_score(t) + 1)