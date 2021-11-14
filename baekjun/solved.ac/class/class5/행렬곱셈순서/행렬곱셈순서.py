import sys

N = int(sys.stdin.readline())
arr = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]
max_value = 2**32
dp = [[0]*N for _ in range(N)]

for i in range(1, N):
    for j in range(N-i):
        dp[j][j+i] = max_value

        for k in range(j, j+i):
            dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + arr[j][0]*arr[k][1]*arr[j+i][1])
    
print(dp[0][N-1])