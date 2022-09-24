import sys

T = int(sys.stdin.readline())
for _ in range(T):
    K = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    dp = [[0]*K for _ in range(K)]

    for i in range(K-1):
        dp[i][i+1] = arr[i] + arr[i+1]
        for j in range(i+2, K):
            dp[i][j] = dp[i][j-1] + arr[j]

    for v in range(2, K):
        for i in range(K-v):
            j = i + v
            dp[i][j] += min([dp[i][k] + dp[k+1][j] for k in range(i, j)])

    print(dp[0][K-1])