import sys
from collections import deque

direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def bfs(r, c, d):
    queue = deque()
    queue.append((r, c, d))
    visit = set()
    visit.add((r, c))

    answer = 1
    while queue:
        r, c, d = queue.popleft()

        cnt_direction = 0
        for i in range(1, 5):
            nd = (d + 4 - i) % 4
            nr, nc = r + direction[nd][0], c + direction[nd][1]

            if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in visit and board[nr][nc] == 0:
                queue.append((nr, nc, nd))
                visit.add((nr, nc))
                answer += 1
                break

            cnt_direction += 1

        if cnt_direction == 4:
            nd = (d + 2) % 4
            nr, nc = r + direction[nd][0], c + direction[nd][1]

            if board[nr][nc] == 1:
                return answer
            queue.append((nr, nc, d))
            visit.add((nr, nc))

N, M = map(int, sys.stdin.readline().split())
R, C, D = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

print(bfs(R, C, D))