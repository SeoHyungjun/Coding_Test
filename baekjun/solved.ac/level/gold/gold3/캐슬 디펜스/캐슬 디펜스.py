import sys
from collections import deque

direction = ((0, -1), (0, 1), (-1, 0))

def bfs(r, c):
    queue = deque([(1, r-1, c)])
    visit = set()
    visit.add((r-1, c))

    min_distance = float('inf')
    min_x, min_y = -1, -1

    while queue:
        d, x, y = queue.popleft()

        if min_distance < d: break
        if board[x][y] == 1:
            if min_distance == float('inf'):
                min_distance = d
                min_x, min_y = x, y
            else:
                if min_y > y:
                    min_x, min_y = x, y

        if d == D: continue
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M): continue
            if (nx, ny) in visit: continue
            queue.append((d+1, nx, ny))
            visit.add((nx, ny))

    return (min_x, min_y)


def attack_simulation(archer):
    dead_enemy = set()

    for archer_row in range(N, 0, -1):
        cur_dead_enemy = set()
        for archer_col in archer:
            near_enemy = bfs(archer_row, archer_col)
            if near_enemy == (-1, -1): continue
            cur_dead_enemy.add(near_enemy)
        for x, y in cur_dead_enemy:
            board[x][y] = 0
        dead_enemy |= cur_dead_enemy

    cnt_dead_enemy = len(dead_enemy)
    for x, y in dead_enemy:
        board[x][y] = 1

    return cnt_dead_enemy

def solve():
    answer = 0
    
    archer = []
    for a in range(M):
        archer.append(a)
        for b in range(a+1, M):
            archer.append(b)
            for c in range(b+1, M):
                archer.append(c)
                answer = max(answer, attack_simulation(archer))
                archer.pop()
            archer.pop()
        archer.pop()

    return answer


N, M, D = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

print(solve())