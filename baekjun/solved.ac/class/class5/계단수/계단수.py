import sys

N = int(sys.stdin.readline())
dp = [[0 for _ in range(1024)] for _ in range(10)]

for i in range(1, 10):
    dp[i][1<<i] = 1

for _ in range(1, N):
    dp_next = [[0 for _ in range(1024)] for _ in range(10)]

    for i in range(10):
        for j in range(1024):
            if i < 9:
                dp_next[i+1][j|1<<(i+1)] += dp[i][j] % 1000000000
            if i > 0:
                dp_next[i-1][j|1<<(i-1)] += dp[i][j] % 1000000000

    dp = dp_next

answer = 0
for i in range(10):
    answer += dp[i][1023] % 1000000000

print(answer%1000000000)