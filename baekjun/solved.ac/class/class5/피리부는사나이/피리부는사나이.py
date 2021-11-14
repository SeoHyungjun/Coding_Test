import sys
from collections import deque

dir = {'U':(-1, 0), 'D':(1, 0), 'L':(0, -1), 'R':(0, 1)}

def bfs(a, b, index_group):
    global board
    queue = deque()
    queue.append((a, b))
    group = set()
    group.add((a, b))

    while queue:
        cur_x, cur_y = queue.popleft()

        next_x, next_y = cur_x + dir[board[cur_x][cur_y]][0], cur_y + dir[board[cur_x][cur_y]][1]
        if (next_x, next_y) in group:
            new_group = index_group + 1
            break
        elif board[next_x][next_y].isdigit():
            new_group = int(board[next_x][next_y])
            break
        queue.append((next_x, next_y))
        group.add((next_x, next_y))

    for x, y in group:
        board[x][y] = str(new_group)
    return new_group

N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

cnt_group = 0
for i in range(N):
    for j in range(M):
        if board[i][j] in dir:
            cnt_group = max(cnt_group, bfs(i, j, cnt_group))

print(cnt_group)