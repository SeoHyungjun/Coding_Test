import sys
import heapq

direction = ((-1, 0), (1, 0), (0, -1), (0, 1))

def check(r, c):
    visit = [[float('inf')]*N for _ in range(N)]
    visit[r][c] = 0
    gvisit[r][c] = True
    q = [((r, c))]
    queue = []
    heapq.heappush(queue, (0, r, c))
    while q:
        x, y = q.pop()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if board[nx][ny] == 0 or visit[nx][ny] == 0:
                continue
            q.append((nx, ny))
            visit[nx][ny] = 0
            heapq.heappush(queue, (0, nx, ny))
            gvisit[nx][ny] = True

    while queue:
        d, x, y = heapq.heappop(queue)
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if visit[nx][ny] <= d+1:
                continue
            if board[nx][ny] == 0:
                visit[nx][ny] = d+1
                heapq.heappush(queue, (d+1, nx, ny))
            elif board[nx][ny] == 1:
                return d
    
    return float('inf')

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = float('inf')
gvisit = [[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] == 0 or gvisit[i][j]:
            continue
        answer = min(answer, check(i, j))
    
print(answer)