import sys
import heapq

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
height = {chr(ord('A')+i) : i for i in range(26)}
height.update({chr(ord('a')+i) : 26+i for i in range(26)})

def solve():
    N, M, T, D = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
    up = [[float('inf')]*M for _ in range(N)]
    up[0][0] = 0
    down = [[float('inf')]*M for _ in range(N)]
    down[0][0] = 0

    queue = []
    heapq.heappush(queue, (0, 0, 0)) # cost, x, y

    while queue:
        cost, x, y = heapq.heappop(queue)

        if not(x == 0 and y == 0) and (up[x][y] > cost or cost >= D):
            continue

        for dx, dy in zip(dxs, dys):
            if not (0 <= x + dx < N and 0 <= y + dy < M) or abs(height[board[x][y]] - height[board[x+dx][y+dy]]) > T:
                continue

            diff = abs(height[board[x][y]] - height[board[x+dx][y+dy]])
            if height[board[x][y]] >= height[board[x+dx][y+dy]]:
                new_cost = cost + 1
            else:
                new_cost = cost + diff**2
                
            if up[x+dx][y+dy] <= new_cost:
                continue
            heapq.heappush(queue, (new_cost, x+dx, y+dy))
            up[x+dx][y+dy] = min(up[x+dx][y+dy], new_cost)

    heapq.heappush(queue, (0, 0, 0))
    while queue:
        cost, x, y = heapq.heappop(queue)

        if not(x == 0 and y == 0) and (down[x][y] > cost or cost >= D):
            continue

        for dx, dy in zip(dxs, dys):
            if not (0 <= x + dx < N and 0 <= y + dy < M) or abs(height[board[x][y]] - height[board[x+dx][y+dy]]) > T:
                continue

            diff = abs(height[board[x][y]] - height[board[x+dx][y+dy]])
            if height[board[x][y]] <= height[board[x+dx][y+dy]]:
                new_cost = cost + 1
            else:
                new_cost = cost + diff**2
                
            if down[x+dx][y+dy] <= new_cost:
                continue
            heapq.heappush(queue, (new_cost, x+dx, y+dy))
            down[x+dx][y+dy] = min(down[x+dx][y+dy], new_cost)

    answer = 0
    for i in range(N):
        for j in range(M):
            cur_time = up[i][j] + down[i][j]

            if cur_time > D:
                continue

            answer = max(answer, height[board[i][j]])

    return answer

print(solve())