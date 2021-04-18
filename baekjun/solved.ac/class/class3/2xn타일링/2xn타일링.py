import sys

N = int(sys.stdin.readline())

dp = [0] * 1001
dp[0] = 1
dp[1] = 1 # 2x1

for i in range(2, N + 1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N]%10007)