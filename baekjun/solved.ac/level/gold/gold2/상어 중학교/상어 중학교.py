import sys
from collections import deque

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def find_biggest_group():
    visit = set()

    answer = []
    for i in range(N):
        for j in range(N):
            if (i, j) in visit or board[i][j] <= 0:
                continue
            cur_cnt, cur_rainbow, cur_visit = bfs(i, j)
            if cur_cnt >= 2:
                answer.append([cur_cnt, cur_rainbow, i, j, cur_visit])
                visit.update(cur_visit)

    if not answer:
        return -1
    answer.sort(key=lambda x :(-x[0], -x[1], -x[2], -x[3]))
    return answer[0]


def bfs(a, b):
    cnt = 1
    color = board[a][b]
    queue = deque([(a, b)])
    visit = set([(a, b)])
    rainbow_cnt = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N and (board[nx][ny] == color or board[nx][ny] == 0) and (nx, ny) not in visit):
                continue
            cnt += 1
            queue.append((nx, ny))
            visit.add((nx, ny))
            if board[nx][ny] == 0:
                rainbow_cnt += 1
    
    return cnt, rainbow_cnt, visit

def delete_group(g):
    for x, y in g:
        board[x][y] = -2


def set_gravity():
    for j in range(N):
        for i in range(N-2, -1, -1):
            if board[i][j] < 0:
                continue
            
            tmp = i
            while tmp + 1 < N and board[tmp+1][j] == -2:
                tmp += 1

            if i == tmp:
                continue

            board[tmp][j] = board[i][j]
            board[i][j] = -2


def turn_left():
    new_board = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[i][j] = board[j][N-1-i]

    return new_board


N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

point = 0
while True:
    group = find_biggest_group()
    if group == -1:
        break
    num, _, _, _, group = group
    point += num**2
    delete_group(group)
    set_gravity()
    board = turn_left()
    set_gravity()
print(point)