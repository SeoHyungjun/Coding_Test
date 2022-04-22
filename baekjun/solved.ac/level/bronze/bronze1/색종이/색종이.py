import sys

board = [[0] * 100 for _ in range(100)]

N = int(sys.stdin.readline())
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())

    for i in range(b, b+10):
        for j in range(a, a+10):
            board[i][j] = 1

answer = 0
for i in range(100):
    answer += sum(board[i])
print(answer)