import sys
from collections import deque
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def change_map():
    global board, key
    for i in range(h+2):
        for j in range(w+2):
            if board[i][j].lower() in key:
                board[i][j] = '.'

def bfs():
    global board, key
    answer = 0
    queue = deque()
    queue.append((0, 0))
    visited = [[False] * (w+2) for _ in range(h+2)]
    visited[0][0] = True

    while queue:
        #print(queue, key)
        #print(*board, sep = '\n')
        x, y = queue.popleft()

        for dx, dy in dir:
            if 0 <= x + dx < h+2 and 0 <= y + dy < w+2 and board[x+dx][y+dy] != '*' and not('A' <= board[x+dx][y+dy] <= 'Z') and not visited[x+dx][y+dy]:
                if 'a' <= board[x+dx][y+dy] <= 'z':
                    key.add(board[x+dx][y+dy])
                    change_map()
                    queue = deque()
                    queue.append((0, 0))
                    visited = [[False] * (w+2) for _ in range(h+2)]
                    visited[0][0] = True
                    continue

                elif board[x+dx][y+dy] == '$':
                    board[x+dx][y+dy] = '.'
                    answer += 1
                queue.append((x+dx, y+dy))
                visited[x+dx][y+dy] = True
    
    return answer

T = int(sys.stdin.readline())
for _ in range(T):
    h, w = map(int, sys.stdin.readline().split())
    board = [['.'] * (w+2)] + [list('.' + sys.stdin.readline().rstrip() + '.') for _ in range(h)] + [['.'] * (w+2)]
    key = set(list(sys.stdin.readline().rstrip()))

    change_map()
    print(bfs())