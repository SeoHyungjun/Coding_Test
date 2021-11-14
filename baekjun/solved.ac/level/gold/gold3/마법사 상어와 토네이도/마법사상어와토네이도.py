import sys
import math
direction = [[0, -1], [1, 0], [0, 1], [-1, 0]]


def move_sand(x, y, dx, dy):
    global board
    cur_sand = board[x+dx][y+dy]
    one_percent_sand = cur_sand / 100
    out_sand = 0

    if dx:
        move_list = [(x, y - 1, 1), (x, y + 1, 1), (x + dx, y - 1, 7),
                    (x + dx, y + 1, 7), (x + dx, y - 2, 2), (x + dx, y + 2, 2),
                    (x + 2 * dx, y - 1, 10), (x + 2 * dx, y + 1, 10), (x + 3 * dx, y, 5)]
    else:
        move_list = [(x - 1, y, 1), (x + 1, y, 1), (x - 1, y + dy, 7),
                    (x + 1, y + dy, 7), (x - 2, y + dy, 2), (x + 2, y + dy, 2),
                    (x - 1, y + 2*dy, 10), (x + 1, y + 2*dy, 10), (x, y + 3 * dy, 5)]

    for next_x, next_y, percent in move_list:
        moved_sand = math.floor(one_percent_sand * percent)
        if 0 <= next_x < N and 0 <= next_y < N:
            board[next_x][next_y] += moved_sand
        else:
            out_sand += moved_sand
        cur_sand -= moved_sand

    a_x, a_y = x + 2*dx, y + 2*dy
    if 0 <= a_x < N and 0 <= a_y < N:
        board[a_x][a_y] += cur_sand
    else:
        out_sand += cur_sand

    board[x + dx][y + dy] = 0

    return out_sand


def tornado():
    global board
    answer = 0
    move_step = 0
    cur_direction = 0

    cur_x, cur_y = N // 2, N // 2
    end_flag = False

    while not end_flag:
        if not cur_direction % 2:
            move_step += 1

        for i in range(move_step):
            dx, dy = direction[cur_direction]
            answer += move_sand(cur_x, cur_y, dx, dy)
            cur_x, cur_y = cur_x + dx, cur_y + dy

            if cur_x == 0 and cur_y == 0:
                end_flag = True
                break

        cur_direction = (cur_direction + 1) % 4

    return answer


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    print(tornado())