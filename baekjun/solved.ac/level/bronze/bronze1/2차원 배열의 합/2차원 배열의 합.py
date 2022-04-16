import sys

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, input().split())) for _ in range(N)]

K = int(sys.stdin.readline())
dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = arr[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

for _ in range(K):
    a, b, c, d = map(int, sys.stdin.readline().split())
    print(dp[c][d] - dp[c][b-1] - dp[a-1][d] + dp[a-1][b-1])