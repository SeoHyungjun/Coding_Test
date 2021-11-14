from collections import deque

dx = [-2, -2, 2, 2, -1, -1, 1, 1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

n = int(input())

def bfs(cx, cy, lx, ly, len):
    visit = [ [0]*len for _ in range(len)]
    queue = deque()
    queue.append((cx, cy, 0))
    visit[cx][cy] = 1

    min = 999999

    while queue:
        x, y, time = queue.popleft()

        if x == lx and y == ly:
            #if min > time:
            #    min = time
            print(time)
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len and 0 <= ny < len and visit[nx][ny] == 0:
                queue.append((nx, ny, time+1))
                visit[nx][ny] = 1

    #print(min)

for _ in range(n):
    l = int(input())

    cur_x, cur_y = map(int, input().split())
    last_x, last_y = map(int, input().split())

    bfs(cur_x, cur_y, last_x, last_y, l)