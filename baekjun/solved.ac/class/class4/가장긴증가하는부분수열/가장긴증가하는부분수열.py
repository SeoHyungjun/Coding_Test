import sys
import bisect

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

dp = [arr[0]]

for i in range(1, N):
    if arr[i] > dp[-1]:
        dp.append(arr[i])

    else:
        dp[bisect.bisect_left(dp, arr[i])] = arr[i]

print(len(dp))