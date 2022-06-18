import sys

direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

M, N = map(int, sys.stdin.readline().split())

board = [[True]*N for _ in range(M)]

x, y = 0, 0
board[0][0] = False
direction_index = 0

answer = 0
while True:
    next_x, next_y = x + direction[direction_index][0], y + direction[direction_index][1]
    if not (0 <= next_x < M and 0 <= next_y < N and board[next_x][next_y]):
        answer += 1
        direction_index = (direction_index + 1) % 4
        next_x, next_y = x + direction[direction_index][0], y + direction[direction_index][1]

        if not board[next_x][next_y]:
            break

    board[next_x][next_y] = False
    x, y = next_x, next_y

print(answer - 1)