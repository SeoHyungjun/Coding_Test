import sys
from collections import defaultdict, deque

N, M = map(int, sys.stdin.readline().split())
degree = [0] * N
graph = defaultdict(list)
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    degree[b-1] += 1
    graph[a-1].append(b-1)

queue = deque()
for i in range(N):
    if degree[i] == 0:
        queue.append(i)

answer = []
while queue:
    cur = queue.popleft()
    answer.append(cur+1)

    for i in range(len(graph[cur])):
        degree[graph[cur][i]] -= 1
        if degree[graph[cur][i]] == 0:
            queue.append(graph[cur][i])

print(*answer)