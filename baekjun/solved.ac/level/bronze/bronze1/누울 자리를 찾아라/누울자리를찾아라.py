import sys

N = int(sys.stdin.readline())
board = ['X'*(N+2)] + ['X' + sys.stdin.readline().rstrip() + 'X' for _ in range(N)] + ['X'*(N+2)]

row, col = 0, 0
for i in range(N+2):
    connected = 0
    for j in range(N+2):
        if board[i][j] == '.':
            connected += 1
        else:
            if connected >= 2:
                row += 1
            connected = 0

for j in range(N+2):
    connected = 0
    for i in range(N+2):
        if board[i][j] == '.':
            connected += 1
        else:
            if connected >= 2:
                col += 1
            connected = 0

print(row, col)