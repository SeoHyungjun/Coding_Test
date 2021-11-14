import sys
from collections import deque
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def change_snake_direction(cur_direction, change_direction):
    if change_direction == 'D':
        cur_direction = (cur_direction + 1) % 4
    else:
        cur_direction = (cur_direction + 3) % 4

    return cur_direction


def find_endgame_time():
    global board
    snake_direction = 0
    move_time = 0

    board[0][0] = 2
    snake = deque()
    snake.append((0, 0))

    index_of_snake_spin = 0
    cur_x, cur_y = 0, 0

    while True:
        if index_of_snake_spin < L and int(snake_spin[index_of_snake_spin][0]) == move_time:
            snake_direction = change_snake_direction(snake_direction, snake_spin[index_of_snake_spin][1])
            index_of_snake_spin += 1

        dx, dy = direction[snake_direction]
        cur_x, cur_y = cur_x + dx, cur_y + dy
        move_time += 1

        if not (0 <= cur_x < N and 0 <= cur_y < N) or board[cur_x][cur_y] == 2:
            break

        if board[cur_x][cur_y] == 0:
            tail_x, tail_y = snake.popleft()
            board[tail_x][tail_y] = 0

        snake.append((cur_x, cur_y))
        board[cur_x][cur_y] = 2

    return move_time


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    board = [[0] * N for _ in range(N)]

    K = int(sys.stdin.readline())
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        board[x-1][y-1] = 1

    L = int(sys.stdin.readline())
    snake_spin = [sys.stdin.readline().rstrip().split() for _ in range(L)]

    print(find_endgame_time())