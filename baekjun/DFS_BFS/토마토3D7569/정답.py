from collections import deque

m, n, h = map(int, input().split())

arr = []
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

for i in range(h):
    arr.append([])
    for _ in range(n):
        arr[i].append(list(map(int, input().split())))

queue = deque()
zero_cnt = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                queue.append((i,j,k))
            elif arr[i][j][k] == 0:
                zero_cnt += 1


def bfs():

    while queue:
        z, y, x = queue.popleft()

        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and arr[nz][ny][nx] == 0:
                arr[nz][ny][nx] = arr[z][y][x] + 1
                queue.append((nz, ny, nx))

    answer = 0

    for i in range(h):
        for j in range(n):
            if 0 in arr[i][j]:
                return -1
            if answer < max(arr[i][j]):
                answer = max(arr[i][j])

    return answer - 1
    
if zero_cnt == 0:
    print(0)
else:
    print(bfs())