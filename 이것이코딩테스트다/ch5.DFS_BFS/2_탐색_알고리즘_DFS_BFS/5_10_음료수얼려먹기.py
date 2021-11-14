dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input())))

result = 2

def dfs(x, y):
    arr[x][y] = result

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
            dfs(nx, ny)

    print(x,y, arr)
    
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            dfs(i, j)
            result += 1

print(result - 2)
