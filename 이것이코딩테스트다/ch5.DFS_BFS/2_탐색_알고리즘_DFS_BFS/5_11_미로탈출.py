#210114 17:10 -> 17:36
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == 0 and ny == 0:
                continue
            
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                print("if", nx, ny)
                queue.append((nx, ny))
                #if nx != 0 and ny != 0:
                arr[nx][ny] = arr[x][y] + 1

        print(arr)
    
    return arr[n-1][m-1]

print(bfs(0, 0))
