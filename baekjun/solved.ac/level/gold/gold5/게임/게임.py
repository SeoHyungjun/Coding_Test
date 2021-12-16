import sys
import heapq
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs(x, y):
    queue = []
    heapq.heappush(queue, (0, -x, -y))
    visit = set()
    visit.add((x, y))

    while queue:
        cost, curx, cury = heapq.heappop(queue)
        curx, cury = -curx, -cury
        if curx == 500 and cury == 500:
            return cost

        for dx, dy in direction:
            if 0 <= curx + dx < 501 and 0 <= cury + dy < 501 and (curx+dx, cury+dy) not in visit:
                if board[curx+dx][cury+dy] == 2:
                    continue
                visit.add((curx+dx, cury+dy))
                heapq.heappush(queue, (cost+board[curx+dx][cury+dy], -(curx+dx), -(cury+dy)))
        
    return -1

board = [[0]*501 for _ in range(501)]
N = int(sys.stdin.readline())
for _ in range(N):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    for i in range(min(x1, x2), max(x1, x2)+1):
        for j in range(min(y1, y2), max(y1, y2)+1):
            board[i][j] = 1
M = int(sys.stdin.readline())
for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    for i in range(min(x1, x2), max(x1, x2)+1):
        for j in range(min(y1, y2), max(y1, y2)+1):
            board[i][j] = 2

print(bfs(0, 0))