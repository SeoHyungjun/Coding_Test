import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr.sort(key = lambda x : x[0])

dp = [arr[0][1]]
for i in range(1, len(arr)):
    if arr[i][1] > dp[-1]:
        dp.append(arr[i][1])
    
    elif arr[i][1] < dp[-1]:
        dp[bisect_left(dp, arr[i][1])] = arr[i][1]

print(N - len(dp))