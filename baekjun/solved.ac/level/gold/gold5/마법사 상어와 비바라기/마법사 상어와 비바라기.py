import sys
from xxlimited import new

direction = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
diagonal = [[-1, -1], [-1, 1], [1, 1], [1, -1]]

def move_rain_cloud(d, s, rain_cloud):
    dx, dy = direction[d-1][0]*s, direction[d-1][1]*s
    new_rain_cloud = set()
    for x, y in rain_cloud:
        new_rain_cloud.add((((x+dx) + 50*N)%N, ((y+dy) + 50*N)%N))

    return new_rain_cloud


def raining(board, rain_cloud):
    for x, y in rain_cloud:
        board[x][y] += 1

    return board


def water_copy(board, rain_cloud):
    for x, y in rain_cloud:
        sum = 0
        for dx, dy in diagonal:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] >= 1:
                sum += 1

        board[x][y] += sum

    return board


def make_rain_cloud(board, rain_cloud):
    new_rain_cloud = set()
    for i in range(N):
        for j in range(N):
            if board[i][j] < 2:
                continue
            new_rain_cloud.add((i, j))

    new_rain_cloud -= rain_cloud
    for x, y in new_rain_cloud:
        board[x][y] -= 2

    return board, new_rain_cloud


N, M = map(int, sys.stdin.readline().split())
rain_cloud = set([(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)])
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
move = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

for d, s in move:
    rain_cloud = move_rain_cloud(d, s, rain_cloud)
    board = raining(board, rain_cloud)
    board = water_copy(board, rain_cloud)
    borad, rain_cloud = make_rain_cloud(board, rain_cloud)

answer = [sum(b) for b in board]
print(sum(answer))