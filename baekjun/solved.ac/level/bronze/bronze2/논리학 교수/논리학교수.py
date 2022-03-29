import sys
from collections import defaultdict

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
cnt = defaultdict(int)

cnt[0] = 0
for i in arr:
    cnt[i] += 1

answer = -1
for i in sorted(cnt.keys(), reverse=True):
    if cnt[i] == i:
        answer = i
        break

print(answer)