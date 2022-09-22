import sys
sys.setrecursionlimit(10**9)

direction = ((-1, 0), (1, 0), (0, -1), (0, 1))

# dfs(x, y) -> (x, y)에서 출발하여 (N-1, M-1)까지 가는 경우의 수
def dfs(x, y):
    if x == N-1 and y == M-1: return 1
    if dp[x][y] != -1: return dp[x][y]

    dp[x][y] = 0
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < N and 0 <= ny < M) or board[x][y] <= board[nx][ny]:
            continue
        dp[x][y] += dfs(nx, ny)

    return dp[x][y]

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[-1]*M for _ in range(N)]

print(dfs(0, 0))