import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

a, b = 0, 0
for i in range(N):
    if 'X' not in board[i]:
        a += 1
    
for i in range(M):
    if 'X' not in [board[j][i] for j in range(N)]:
        b += 1

print(max(a, b))