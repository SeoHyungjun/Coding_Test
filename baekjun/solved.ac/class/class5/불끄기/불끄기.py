import sys
dir = [(-1, 0), (1, 0), (0, 0), (0, -1), (0, 1)]

def solve(cnt):
    global answer, board
    tmp = []
    
    for i in range(1, 10):
        for j in range(10):
            if board[i-1][j] == 'O':
                tmp.append((i, j))
                change(i, j)
                cnt += 1

    if 'O' not in board[9]:
        answer = min(answer, cnt)

    for i, j in tmp:
        change(i, j)

def change(i, j):
    global board
    for dx, dy in dir:
        if 0 <= i + dx < 10 and 0 <= j + dy < 10:
            if board[i+dx][j+dy] == '#':
                board[i+dx][j+dy] = 'O'
            else:
                board[i+dx][j+dy] = '#'

def dfs(i, cnt):
    global board, answer
    if i >= 10:
        solve(cnt)
        return
    
    #바꾸고
    change(0, i)
    dfs(i+1, cnt+1)
    #원래대로
    change(0, i)
    dfs(i+1, cnt)

board = [list(sys.stdin.readline().rstrip()) for _ in range(10)]
answer = 101
dfs(0, 0)

if answer == 101:
    print(-1)
else:
    print(answer)