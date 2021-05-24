import sys

R, C, T = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

air = []
for i in range(R):
    if board[i][0] == -1:
        air.append(i)

def spread():
    new_board = [[0]*C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                div_dust = board[i][j] // 5
                spread_cnt = 0

                for dx, dy in dir:
                    nx, ny = i+dx, j+dy
                    if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != -1:
                        new_board[nx][ny] += div_dust
                        spread_cnt += 1

                new_board[i][j] -= div_dust*spread_cnt

    for i in range(R):
        for j in range(C):
            board[i][j] += new_board[i][j]


def air_cal():
    cur = [air[0]-1, 0]

    while cur[0] > 0:
        board[cur[0]][cur[1]] = board[cur[0]-1][cur[1]]
        cur[0] -= 1

    while cur[1] < C-1:
        board[cur[0]][cur[1]] = board[cur[0]][cur[1]+1]
        cur[1] += 1

    while cur[0] < air[0]:
        board[cur[0]][cur[1]] = board[cur[0]+1][cur[1]]
        cur[0] += 1

    while cur[1] > 1:
        board[cur[0]][cur[1]] = board[cur[0]][cur[1]-1]
        cur[1] -= 1

    board[air[0]][1] = 0

    cur = [air[1]+1, 0]

    while cur[0] < R-1:
        board[cur[0]][cur[1]] = board[cur[0]+1][cur[1]]
        cur[0] += 1

    while cur[1] < C-1:
        board[cur[0]][cur[1]] = board[cur[0]][cur[1]+1]
        cur[1] += 1

    while cur[0] > air[1]:
        board[cur[0]][cur[1]] = board[cur[0]-1][cur[1]]
        cur[0] -= 1

    while cur[1] > 1:
        board[cur[0]][cur[1]] = board[cur[0]][cur[1]-1]
        cur[1] -= 1
    board[cur[0]][cur[1]] = 0

for _ in range(T):
    spread()
    air_cal()

answer = 0
for b in board:
    answer += sum(b)

print(answer + 2)