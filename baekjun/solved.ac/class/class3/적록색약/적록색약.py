import sys
from collections import deque

def DFS(board, visit, x, y, cnt, N):
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    tmp = board[x][y]
    queue = deque()
    queue.append((x, y, cnt))

    while queue:
        cur_x, cur_y, cnt = queue.popleft()

        for dx, dy in dir:
            if 0 <= cur_x+dx < N and 0<= cur_y+dy < N and (not visit[cur_x+dx][cur_y+dy]) and board[cur_x+dx][cur_y+dy] == tmp:
                queue.append((cur_x+dx, cur_y+dy, cnt))
                visit[cur_x+dx][cur_y+dy] = cnt


N = int(sys.stdin.readline())
normal_board = []
rg_board = []
normal = [[False] * N for _ in range(N)]
rg = [[False] * N for _ in range(N)]

for _ in range(N):
    inp = sys.stdin.readline().rstrip()
    normal_board.append(list(inp))
    rg_board.append(list(inp.replace('R', 'G')))

normal_cnt = 1
rg_cnt = 1
for i in range(N):
    for j in range(N):
        if not normal[i][j]:
            DFS(normal_board, normal, i, j, normal_cnt, N)
            normal_cnt += 1

        if not rg[i][j]:
            DFS(rg_board, rg, i, j, rg_cnt, N)
            rg_cnt += 1

print(normal_cnt-1, rg_cnt-1)