import sys

def avail():
    for start in range(N):
        k = start
        for j in range(H):
            if graph[j][k]: k += 1
            elif k > 0 and graph[j][k-1]: k -= 1
        if k != start: return False
    return True

def dfs(cnt, x, y):
    global answer
    if avail():
        answer = min(answer, cnt)
        return
    if cnt == 3 or answer <= cnt: return

    for i in range(x, H):
        if i == x: k = y
        else: k = 0
        for j in range(k, N-1):
            if graph[i][j] or graph[i][j+1]: continue
            if j > 0 and graph[i][j-1]: continue
            graph[i][j] = True
            dfs(cnt+1, i, j+2)
            graph[i][j] = False

def solve():
    global answer
    if M == 0: answer = 0

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a-1][b-1] = True

    answer = 4
    dfs(0, 0, 0)

N, M, H = map(int, sys.stdin.readline().split())
graph = [[False]*N for _ in range(H)]
answer = 4

solve()
print(answer if answer < 4 else -1)