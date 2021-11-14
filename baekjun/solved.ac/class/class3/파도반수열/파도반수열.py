# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9
import sys

T = int(sys.stdin.readline())

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = dp[3] + dp[1]
dp[5] = dp[4]

for i in range(6, 101):
    dp[i] = dp[i-1] + dp[i-5]
# dp[6] = dp[5] + dp[1]
# dp[7] = dp[6] + dp[2]
# dp[8] = dp[7] + dp[3]
# dp[9] = dp[8] + dp[4]
# dp[10] = dp[9] + dp[5]
# dp[11] = dp[10] + dp[6]


for _ in range(T):
    N = int(sys.stdin.readline())
    print(dp[N])