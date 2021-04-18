import sys

N = int(sys.stdin.readline())
dp = [0, 1]

for i in range(2, N+1):
    min_cnt = float('inf')
    j = 1

    while j**2 <= i:
        min_cnt = min(min_cnt, dp[ i - j**2] + 1)
        j += 1

    dp.append(min_cnt)

print(dp[N])