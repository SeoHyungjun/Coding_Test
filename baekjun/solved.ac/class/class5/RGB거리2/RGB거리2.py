import sys

def solve():
    answer = float('inf')
    for init_color in range(3):
        for i in range(3):
            if i == init_color:
                dp[0][i] = cost[0][i]
            else:
                dp[0][i] = float('inf')

        for i in range(1, N):
                dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
                dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
                dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])

        for i in range(3):
            if i != init_color:
                answer = min(answer, dp[N-1][i])

    return answer

N = int(sys.stdin.readline())
cost = []
dp = [[float('inf'), float('inf'), float('inf')] for _ in range(N)]
for _ in range(N):
    cost.append(list(map(int, sys.stdin.readline().split())))

print(solve())