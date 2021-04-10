import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

go = []

for i in range(N):
    visit = [0] * N
    queue = deque()
    for j in range(N):
        if not visit[j] and graph[i][j] == 1:
            queue.append(j)
            visit[j] = 1
    
    while queue:
        cur = queue.popleft()

        for j in range(N):
            if not visit[j] and graph[cur][j] == 1:
                queue.append(j)
                visit[j] = 1
    
    go.append(visit)

for i in go:
    for j in i:
        print(j, end = ' ')
    print()
