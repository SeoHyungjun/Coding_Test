#knapsack 문제
import sys

N, M = map(int, sys.stdin.readline().split())
memory = [0] + list(map(int, sys.stdin.readline().split()))
cost = [0] + list(map(int, sys.stdin.readline().split()))

dp = [[0] * (sum(cost)+1) for _ in range(N+1)]

result = sum(cost)
for i in range(1, N+1):
    for j in range(1, sum(cost)+1):
        if j < cost[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(memory[i] + dp[i-1][j-cost[i]], dp[i-1][j])

        if dp[i][j] >= M:
            result = min(result, j)

print(result if M != 0 else 0)