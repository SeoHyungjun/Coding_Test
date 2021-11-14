import sys

def solve():
    for i in range(2, N+1):
        dp[i] = dp[i-1] + 1
        prev[i] = i-1

        if i % 3 == 0 and dp[i//3] + 1 < dp[i]:
            dp[i] = dp[i//3] + 1
            prev[i] = i//3
        if i % 2 == 0 and dp[i//2] + 1 < dp[i]:
            dp[i] = dp[i//2] + 1
            prev[i] = i//2

N = int(sys.stdin.readline())
dp = [0] * (N+1)
prev = [-1] * (N+1)
solve()
print(dp[N])
while N > 0:
    print(N, end = ' ')
    N = prev[N]