import sys
from collections import deque

direction = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]

def check_top(i, j):
    global visit
    visit[i][j] = True
    is_top = True
    
    queue = deque()
    queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for dx, dy in direction:
            if not (0 <= x + dx < N and 0 <= y +dy < M):
                continue

            if board[x+dx][y+dy] == board[i][j]:
                if visit[x+dx][y+dy]:
                    continue

                visit[x+dx][y+dy] = True
                queue.append((x+dx, y+dy))

            elif board[x+dx][y+dy] > board[i][j]:
                is_top = False

    return is_top

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visit = [[False] * M for _ in range(N)]

answer = 0

for i in range(N):
    for j in range(M):
        if not visit[i][j]:
            if check_top(i, j) and board[i][j] != 0:
                answer += 1

print(answer)