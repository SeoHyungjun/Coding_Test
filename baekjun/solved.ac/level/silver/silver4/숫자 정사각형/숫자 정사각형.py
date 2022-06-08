import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

answer = 1
for i in range(N):
    for j in range(M):
        for size in range(1, min(N, M)):
            if i + size < N and j + size < M and board[i][j] == board[i+size][j] == board[i][j+size] == board[i+size][j+size]:
                answer = max(answer, (size+1)**2)

print(answer)