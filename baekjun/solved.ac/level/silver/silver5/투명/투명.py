import sys

N, M = map(int, sys.stdin.readline().split())
board = [[0]*100 for _ in range(100)]

for _ in range(N):
    a, b, c, d = map(int, sys.stdin.readline().split())
    for i in range(a-1, c):
        for j in range(b-1, d):
            board[i][j] += 1

answer = 0
for i in range(100):
    for j in range(100):
        if board[i][j] > M:
            answer += 1

print(answer)