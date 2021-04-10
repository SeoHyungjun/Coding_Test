import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
visit = [False] * (N+1)


for _ in range(M):
    U, V = map(int, sys.stdin.readline().split())
    graph[U].append(V)
    graph[V].append(U)
    
cnt = 0
for i in range(1, N+1):
    if not visit[i]:
        queue = deque()
        queue.append(i)
        visit[i] = True
        cnt += 1

        while queue:
            cur = queue.popleft()

            for j in graph[cur]:
                if not visit[j]:
                    visit[j] = True
                    queue.append(j)

print(cnt)