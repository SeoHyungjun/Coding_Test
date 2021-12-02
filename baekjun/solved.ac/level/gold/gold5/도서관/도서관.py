import sys
from bisect import bisect_left

N, M = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))

pivot = bisect_left(arr, 0)
minus, plus = arr[:pivot], arr[pivot:]
tmp_max = 0
answer = 0

for i in range(0, len(minus), M):
    answer += 2*abs(minus[i])
    tmp_max = max(tmp_max, abs(minus[i]))

for i in range(len(plus)-1, -1, -M):
    answer += 2*plus[i]
    tmp_max = max(tmp_max, plus[i])

print(answer - tmp_max)