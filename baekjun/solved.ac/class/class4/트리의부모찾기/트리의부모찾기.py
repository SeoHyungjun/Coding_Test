import sys
from collections import deque

N = int(sys.stdin.readline())
graph = {i:[] for i in range(N)}

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

parent = [0]*N
parent[0] = -1
queue = deque([0])

while queue:
    cur = queue.popleft()

    for i in graph[cur]:
        if parent[cur] != i:
            parent[i] = cur
            queue.append(i)

for i in parent[1:]:
    print(i+1)