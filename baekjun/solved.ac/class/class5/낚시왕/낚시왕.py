import sys
dir = {1:(-1, 0), 2:(1, 0), 3:(0, 1), 4:(0, -1)}

def move_shark():
    global board, shark
    new_board = [[-1]*C for _ in range(R)]
    deleted_shark = []

    for i in shark.keys():
        speed, direction, size, x, y = shark[i]
        board[x][y] = -1

        """
        for _ in range(speed):
            if not (0 <= x + dir[direction][0] < R and 0 <= y + dir[direction][1] < C):
                direction = direction-1 if direction%2 == 0 else direction+1
            x += dir[direction][0]
            y += dir[direction][1]
        """

        leave_speed = speed
        while not (0 <= x + dir[direction][0]*leave_speed < R and 0 <= y + dir[direction][1]*leave_speed < C):
            if direction == 1:
                leave_speed -= x
                x = 0

            elif direction == 2:
                leave_speed -= R-1 - x
                x = R-1

            elif direction == 3:
                leave_speed -= C-1 - y
                y = C-1

            else:
                leave_speed -= y
                y = 0
                
            direction = direction-1 if direction%2 == 0 else direction+1

        x += dir[direction][0] * leave_speed
        y += dir[direction][1] * leave_speed
                
        if new_board[x][y] != -1:
            if shark[new_board[x][y]][2] < size:
                deleted_shark.append(new_board[x][y])
                new_board[x][y] = i
                shark[i] = [speed, direction, size, x, y]
            else:
                deleted_shark.append(i)
        else:
            new_board[x][y] = i
            shark[i] = [speed, direction, size, x, y]

    for i in deleted_shark:
        del shark[i]
    
    board = new_board


R, C, M = map(int, sys.stdin.readline().split())
board = [[-1] * C for _ in range(R)]
shark = {}
answer = 0

for i in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    if d == 1 or d == 2:
        s %= (R-1)*2
    else:
        s %= (C-1)*2
    shark[i] = [s, d, z, r-1, c-1]
    board[r-1][c-1] = i

for j in range(C):
    for i in range(R):
        if board[i][j] != -1:
            answer += shark[board[i][j]][2]
            del shark[board[i][j]]
            board[i][j] = -1
            break
    move_shark()

print(answer)