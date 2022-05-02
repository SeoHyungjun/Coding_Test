import sys

C, N = map(int, sys.stdin.readline().split())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [float('inf')] * (C+100)
dp[0] = 0

for cost, customer in info:
    for i in range(customer, C+100):
        dp[i] = min(dp[i], dp[i-customer] + cost)

print(min(dp[C:]))