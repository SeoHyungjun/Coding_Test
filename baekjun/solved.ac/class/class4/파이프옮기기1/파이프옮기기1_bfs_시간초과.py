import sys
from collections import deque
LANDSCAPE = 0
PORTRAIT = 1
DIAGONAL = 2

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0

queue = deque()
queue.append((LANDSCAPE, 0, 1))

while queue:
    dir, X, Y = queue.popleft()

    if  X == N-1 and Y == N-1:
        answer += 1
        continue

    if dir == LANDSCAPE:
        if Y+1 < N and board[X][Y+1] == 0:
            queue.append((LANDSCAPE, X, Y+1))

        if X+1 < N and Y+1 < N and board[X][Y+1] == 0 and board[X+1][Y] == 0 and board[X+1][Y+1] == 0:
            queue.append((DIAGONAL, X+1, Y+1))

    elif dir == PORTRAIT:
        if X+1 < N and board[X+1][Y] == 0:
            queue.append((PORTRAIT, X+1, Y))

        if X+1 < N and Y+1 < N and board[X][Y+1] == 0 and board[X+1][Y] == 0 and board[X+1][Y+1] == 0:
            queue.append((DIAGONAL, X+1, Y+1))
    else:
        if X+1 < N and board[X+1][Y] == 0:
            queue.append((PORTRAIT, X+1, Y))

        if Y+1 < N and board[X][Y+1] == 0:
            queue.append((LANDSCAPE, X, Y+1))

        if X+1 < N and Y+1 < N and board[X][Y+1] == 0 and board[X+1][Y] == 0 and board[X+1][Y+1] == 0:
            queue.append((DIAGONAL, X+1, Y+1))

print(answer)