import sys

N = int(sys.stdin.readline())
board = [list(sys.stdin.readline().strip()) for _ in range(N)]
answer = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not board[i][j].isdigit():
            continue

        answer[i][j] = '*'
        for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
            next_x, next_y = i + dx, j + dy

            if not (0 <= next_x < N and 0 <= next_y < N and answer[next_x][next_y] != '*'):
                continue
            answer[next_x][next_y] += int(board[i][j])

for i in range(N):
    tmp = ''
    for j in range(N):
        if str(answer[i][j]).isdigit() and answer[i][j] >= 10:
            tmp += 'M'
        else:
            tmp += str(answer[i][j])

    print(tmp)