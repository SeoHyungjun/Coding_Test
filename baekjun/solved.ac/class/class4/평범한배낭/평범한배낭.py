import sys

N, K = map(int, sys.stdin.readline().split())

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    W, V = map(int, sys.stdin.readline().split())
    for j in range(1, K+1):
        if j < W:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], V + dp[i-1][j-W])

print(dp[N][K])