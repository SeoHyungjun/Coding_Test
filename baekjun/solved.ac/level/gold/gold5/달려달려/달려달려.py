import sys
input = sys.stdin.readline

N, M = map(int, input().split())

distance = [int(input()) for _ in range(N)]
dp = [[[0 , 0] for _ in range(M + 2)] for _ in range(2)]

for i in range(1, N + 1):
    dp[i % 2][0][0] = max(dp[(i - 1) % 2][1][0], dp[(i - 1) % 2][1][1], dp[(i - 1) % 2][0][0])
    dp[i % 2][1][0] = max(dp[(i - 1) % 2][2][0], dp[(i - 1) % 2][2][1])
    dp[i % 2][1][1] = max(dp[(i - 1) % 2][0][0] + distance[i - 1], dp[(i - 1) % 2][0][1])
    
    for j in range(2, M):
        dp[i % 2][j][0] = max(dp[(i - 1) % 2][j + 1][0], dp[(i - 1) % 2][j + 1][1])
        dp[i % 2][j][1] = dp[(i - 1) % 2][j - 1][1] + distance[i - 1]

print(max(dp[0][0][0], dp[1][0][0]))