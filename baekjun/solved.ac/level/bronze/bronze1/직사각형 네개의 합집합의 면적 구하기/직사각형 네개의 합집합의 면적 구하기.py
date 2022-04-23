import sys

board = [[0]*101 for _ in range(101)]
for _ in range(4):
    a, b, c, d = map(int, sys.stdin.readline().split())

    for y in range(b, d):
        for x in range(a, c):
            board[y][x] = 1

answer = 0
for i in range(101):
    answer += sum(board[i])

print(answer)