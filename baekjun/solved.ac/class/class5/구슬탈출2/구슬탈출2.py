import sys
from collections import deque

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    global answer
    queue = deque()
    queue.append((0, RED_X, RED_Y, BLUE_X, BLUE_Y))
    visit = set()
    visit.add((RED_X, RED_Y, BLUE_X, BLUE_Y))

    while queue:
        cnt, rx, ry, bx, by = queue.popleft()
        if cnt > 10:
            continue

        for dx, dy in dir:
            red_state = False
            blue_state = False
            nrx, nry = rx, ry
            while True:
                nrx += dx
                nry += dy
                if board[nrx][nry] == '#':
                    nrx -= dx
                    nry -= dy
                    break
                elif board[nrx][nry] == 'O':
                    red_state = True
                    break

            nbx, nby = bx, by
            while True:
                nbx += dx
                nby += dy
                if board[nbx][nby] == '#':
                    nbx -= dx
                    nby -= dy
                    break
                elif board[nbx][nby] == 'O':
                    blue_state = True
                    break

            if nrx == nbx and nry == nby:
                if abs(nrx-rx) + abs(nry-ry) < abs(nbx-bx) + abs(nby-by):
                    nbx -= dx
                    nby -= dy
                else:
                    nrx -= dx
                    nry -= dy

            if red_state and not blue_state:
                if answer == -1:
                    answer = cnt + 1
                else:
                    answer = min(answer, cnt+1)
                return
            elif not red_state and not blue_state and (nrx, nry, nbx, nby) not in visit:
                visit.add((nrx, nry, nbx, nby))
                queue.append((cnt+1, nrx, nry, nbx, nby))

N, M = map(int, sys.stdin.readline().split())
board = []
answer = -1
for i in range(N):
    board.append(list(sys.stdin.readline().rstrip()))
    for j in range(M):
        if board[i][j] == 'R':
            RED_X, RED_Y = i, j
            board[i][j] = '.'
        elif board[i][j] == 'B':
            BLUE_X, BLUE_Y = i, j
            board[i][j] = '.'

bfs()
if answer > 10:
    answer = -1
print(answer)