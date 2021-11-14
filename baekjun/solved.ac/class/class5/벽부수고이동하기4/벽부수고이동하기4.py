import sys
from collections import deque
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y, index_group):
    queue = deque([(x, y)])
    group[x][y] = index_group
    cnt = 1

    while queue:
        cur_x, cur_y = queue.popleft()

        for dx, dy in dir:
            next_x, next_y = cur_x + dx, cur_y + dy

            if 0 <= next_x < N and 0 <= next_y < M and board[next_x][next_y] == 0 and group[next_x][next_y] == -1:
                group[next_x][next_y] = index_group
                queue.append((next_x, next_y))
                cnt += 1

    dic_group[index_group] = cnt

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
group = [[-1] * M for _ in range(N)]
dic_group = {}

index_group = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0 and group[i][j] == -1:
            dfs(i, j, index_group)
            index_group += 1

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            visit_group = set()
            cnt = 1
            for dx, dy in dir:
                if 0 <= i+dx < N and 0 <= j+dy < M and group[i+dx][j+dy] != -1 and group[i+dx][j+dy] not in visit_group:
                    cnt += dic_group[group[i+dx][j+dy]]
                    visit_group.add(group[i+dx][j+dy])
            board[i][j] = cnt % 10

for b in board:
    print(*b, sep='')