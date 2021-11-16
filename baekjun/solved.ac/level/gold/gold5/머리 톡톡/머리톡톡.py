import sys
from collections import defaultdict

N = int(sys.stdin.readline())
arr = [0] * N
cnt = defaultdict(int)
answer = defaultdict(int)
max_value = 0

for i in range(N):
    arr[i] = int(sys.stdin.readline())
    cnt[arr[i]] += 1
    max_value = max(max_value, arr[i])

for k, v in cnt.items():
    answer[k] += v - 1
    for i in range(k+k, max_value+1, k):
        if i in cnt:
            answer[i] += v

for a in arr:
    print(answer[a])