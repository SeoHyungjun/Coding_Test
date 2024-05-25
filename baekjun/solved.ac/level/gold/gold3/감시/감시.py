import sys

# baekjoon 15683 gold3

N, M = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().split()) for _ in range(N)]
answer = N * M
coordinate = []
direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
fill_direction = {'1': [(True, False, False, False), (False, True, False, False), (False, False, True, False), (False, False, False, True)],
                  '2': [(True, True, False, False), (False, False, True, True)],
                  '3': [(True, False, True, False), (False, True, True, False), (False, True, False, True), (True, False, False, True)],
                  '4': [(True, True, True, False), (True, True, False, True), (True, False, True, True), (False, True, True, True)],
                  '5': [(True, True, True, True)]}


# dir = [left, right, up, down]
def fill(board, x, y, dir):
    new_board = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            new_board[i][j] = board[i][j]
    
    for idx, cur in enumerate(dir):
        if not cur: continue
        next_x, next_y = x, y

        while True:
            next_x, next_y = next_x + direction[idx][0], next_y + direction[idx][1]

            if not (next_x >= 0 and next_y >= 0 and next_x < N and next_y < M): break
            if new_board[next_x][next_y] == '6': break
            if new_board[next_x][next_y] != '0': continue

            new_board[next_x][next_y] = '#'

    return new_board


def check(board):
    global answer
    sum = 0

    for i in range(N):
        for j in range(M):
            if board[i][j] == '0':
                sum += 1

    answer = min(answer, sum)


def dfs(depth, board):
    #print(depth)
    #print(*board, sep='\n')

    if depth >= len(coordinate): 
        check(board)
        return

    x, y = coordinate[depth]
    for cur_direction in fill_direction[board[x][y]]:
        new_board = fill(board, x, y, cur_direction)
        dfs(depth + 1, new_board)


for i in range(N):
    for j in range(M):
        if arr[i][j] == '0' or arr[i][j] == '6': continue
        coordinate.append((i, j))

dfs(0, arr)
print(answer)
