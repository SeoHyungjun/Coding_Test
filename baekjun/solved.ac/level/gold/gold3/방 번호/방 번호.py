import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

dp = [-1] * (M+1)
for i in range(N-1, -1, -1):
    for j in range(arr[i], M+1):
        dp[j] = max(dp[j], dp[j-arr[i]]*10 + i, i)

print(dp[M])