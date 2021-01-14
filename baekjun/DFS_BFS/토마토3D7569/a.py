# 210114 17:53
from collections import deque

m, n, h= map(int, input().split())

arr = []
for _ in range(n*h):
    arr.append(list(map(int, input().split())))

dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
dz = [-1*n, n, 0, 0, 0, 0]

tomato = deque()

def dfs():
    check = 0
    for i in range(n*h):
        if 0 not in arr[i]:
            check += 1

    if check == n*h:
        return 0

    while tomato:
        x, y = tomato.popleft()

        for i in range(6):
            nx = x + dz[i] + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h*n and 0 <= ny < m and arr[nx][ny] == 0: 
                arr[nx][ny] = arr[x][y] + 1
                tomato.append((nx, ny))

        #print(arr)

    result = 0
    for i in range(n*h):
        #print(arr[i])
        if 0 in arr[i]:
            return -1
        if result < max(arr[i]):
            result = max(arr[i])

    return result - 1

for i in range(n*h):
    for j in range(m):
        if arr[i][j] == 1:
            tomato.append((i,j))

print(dfs())