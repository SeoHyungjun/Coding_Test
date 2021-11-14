import sys
from collections import deque

N = int(sys.stdin.readline())

board = []
for i in range(N):
    bo = list(map(int,sys.stdin.readline().split()))
    board.append(bo)

    if 9 in bo:
        baby_shark = (i, bo.index(9), 2)


def bfs(baby):
    dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    size = baby[2]
    visit = set()
    queue = deque()
    queue.append(((baby[0], baby[1]), 0))
    visit.add((baby[0], baby[1]))
    avail = []

    while queue:
        cur, cnt = queue.popleft()
        #print(cur, cnt, visit)

        for dx, dy in dir:
            if ((cur[0]+dx, cur[1]+dy) not in visit) and 0 <= cur[0] + dx < N and 0 <= cur[1] + dy < N:
                if board[cur[0]+dx][cur[1]+dy] == 0 or board[cur[0]+dx][cur[1]+dy] == size:
                    queue.append(((cur[0]+dx, cur[1]+dy), cnt + 1))
                    visit.add((cur[0]+dx, cur[1]+dy))
                elif board[cur[0]+dx][cur[1]+dy] < size:
                    avail.append((cur[0]+dx, cur[1]+dy, cnt+1))
                    visit.add((cur[0]+dx, cur[1]+dy))

    return avail

answer = 0
board[baby_shark[0]][baby_shark[1]] = 0
size = baby_shark[2]
eat = 0

while True:
    result = bfs(baby_shark)

    if len(result) == 0:
        print(answer)
        break

    else:
        result = sorted(result, key = lambda x: (x[2], x[0], x[1]))
        answer += result[0][2]
        eat += 1
        if eat == size:
            size += 1
            eat = 0
        baby_shark = (result[0][0], result[0][1], size)
        board[result[0][0]][result[0][1]] = 0
        








