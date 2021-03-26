import sys

T = int(sys.stdin.readline())
dp = {0:(1, 0), 1:(0, 1)}

def fibo(n):
    if n-1 not in dp:
        fibo(n-1)
    if n-2 not in dp:
        fibo(n-2)
    dp[n] = (dp[n-1][0] + dp[n-2][0], dp[n-1][1] + dp[n-2][1])

for _ in range(T):
    N = int(sys.stdin.readline())
    if N not in dp:
        fibo(N)

    print(dp[N][0], dp[N][1])
