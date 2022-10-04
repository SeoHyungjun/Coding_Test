import sys
from collections import deque

move_horse = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
move_monkey = ((-1, 0), (1, 0), (0, -1), (0, 1))

def solve():
    queue = deque([(0, 0, 0, 0)])
    
    while queue:
        cnt, k, x, y = queue.popleft()
        if x == N-1 and y == M-1: return cnt

        for dx, dy in move_monkey:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M): continue
            if board[nx][ny] == 1 or visit[k][nx][ny]: continue
            queue.append((cnt+1, k, nx, ny))
            visit[k][nx][ny] = True

        if k == K: continue
        for dx, dy in move_horse:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M): continue
            if board[nx][ny] == 1 or visit[k+1][nx][ny]: continue
            queue.append((cnt+1, k+1, nx, ny))
            visit[k+1][nx][ny] = True

    return -1

K = int(sys.stdin.readline())
M, N = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visit = [[[False]*M for _ in range(N)] for _ in range(K+1)]

print(solve())