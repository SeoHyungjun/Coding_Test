import sys
input = sys.stdin.readline
import heapq

a, b = map(int, input().split())
n, m = map(int, input().split())

graph = {}
for i in range(n):
    graph[i] = []

for _ in range(m):
    start, end = map(int, input().split())
    graph[start-1].append(end-1)
    graph[end-1].append(start-1)

queue = []
heapq.heappush(queue, (0, a-1))
changes = [float('inf')] * n
changes[a-1] = 0

while queue:
    dis, st = heapq.heappop(queue)

    for i in graph[st]:
        if changes[i] > dis + 1:
            changes[i] = dis + 1
            heapq.heappush(queue, (dis+1, i))

if changes[b-1] == float('inf'):
    print(-1)
else:
    print(changes[b-1])