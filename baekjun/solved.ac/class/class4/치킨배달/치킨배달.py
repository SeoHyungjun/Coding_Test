import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

board = []
house = []
chicken = []
answer = float('inf')

for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N):
        if board[i][j] == 1:
            house.append((i, j))
        elif board[i][j] == 2:
            chicken.append((i, j))

for leave_chicken in list(combinations(chicken, M)):
    cnt = 0
    for x, y in house:
        distance = float('inf')
        for cx, cy in leave_chicken:
            distance = min(distance, abs(cx - x) + abs(cy - y))

        cnt += distance
    answer = min(answer, cnt)
print(answer)

