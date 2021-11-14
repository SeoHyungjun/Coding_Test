# 19:10 -> 19:31

import sys
sys.setrecursionlimit(10**6)

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N = int(sys.stdin.readline())
board = []
max_live = 0

def check(x, y):
    if dp[x][y]:
        return dp[x][y]

    dp[x][y] = 1
    for dx, dy in dir:
        if 0 <= x + dx < N and 0 <= y + dy < N and board[x+dx][y+dy] > board[x][y]:
            dp[x][y] = max(dp[x][y], check(x+dx, y+dy) + 1)

    return dp[x][y]

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
dp = [[0] * N for _ in range(N)] 

for i in range(N):
    for j in range(N):
        max_live = max(max_live, check(i, j))

print(max_live)