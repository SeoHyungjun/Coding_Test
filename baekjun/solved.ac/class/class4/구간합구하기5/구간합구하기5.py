import sys

N, M = map(int, sys.stdin.readline().split())

board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
    board[0][i] += board[0][i-1]
    board[i][0] += board[i-1][0]

for i in range(1, N):
    for j in range(1, N):
        board[i][j] += board[i][j-1] + board[i-1][j] - board[i-1][j-1]

for _ in range(M):
    a, b, c, d = map(int, sys.stdin.readline().split())

    sum = board[c-1][d-1]
    if a != 1:
        sum -= board[a-2][d-1]
    if b != 1:
        sum -= board[c-1][b-2]

    if a != 1 and b!= 1:
        sum += board[a-2][b-2]

    print(sum)