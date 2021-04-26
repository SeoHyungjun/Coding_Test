import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
board = []

def make_air():
    queue = deque()
    queue.append((0,0))

    while queue:
        x = queue.popleft()
        x, y = x[0], x[1]
        for dx, dy in dir:
            if 0 <= x+dx < N and 0 <= y+dy < M and board[x+dx][y+dy] == 0:
                board[x+dx][y+dy] = 2
                queue.append((x+dx, y+dy))

def decrease():
    remove_cheese = set()

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                check = 0
                for dx, dy in dir:
                    if board[i+dx][j+dy] == 2:
                        check += 1
                if check >= 2:
                    remove_cheese.add((i,j))

    for x, y in remove_cheese:
        board[x][y] = 2
        queue = deque()
        queue.append((x, y))
        while queue:
            new = queue.popleft()
            x, y = new[0], new[1]
            for dx, dy in dir:
                if 0 <= x+dx < N and 0 <= y+dy < M and board[x+dx][y+dy] == 0:
                    board[x+dx][y+dy] = 2
                    queue.append((x+dx, y+dy))
    return len(remove_cheese)

cheese_cnt = 0
time = 0

for _ in range(N):
    in_board = list(map(int, sys.stdin.readline().split()))
    board.append(in_board)
    cheese_cnt += in_board.count(1)

make_air()
while cheese_cnt > 0:
    cheese_cnt -= decrease()
    time += 1

print(time)