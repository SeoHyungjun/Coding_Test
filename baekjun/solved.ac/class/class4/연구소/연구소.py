import sys
from collections import deque
from copy import deepcopy

dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
answer = 0
virus = []

def bfs():
    global answer
    nboard = deepcopy(board)
    for v in virus:
        queue.append(v)

    while queue:
        x, y = queue.popleft()

        for dx, dy in dir:
            if 0 <= x + dx < N and 0 <= y + dy < M and nboard[x+dx][y+dy] == 0:
                nboard[x+dx][y+dy] = 2
                queue.append((x+dx, y+dy))

    cnt = 0
    for n in nboard:
        cnt += n.count(0)
    answer = max(answer, cnt)

def wall(x):
    if x == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                wall(x+1)
                board[i][j] = 0

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            virus.append((i, j))
queue = deque()
wall(0)
print(answer)
