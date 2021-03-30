import sys
import heapq
input = sys.stdin.readline
n, m, k, s = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

queue = []
heapq.heappush(queue, (0, s))
distance = [float('inf')] * (n+1)
check = [False] * (n+1)
distance[s] = 0
check[s] = True

while queue:
    dis, curr = heapq.heappop(queue)

    for ci in graph[curr]:
        if not check[ci] and dis+1 < distance[ci]:
            distance[ci] = dis+1
            heapq.heappush(queue, (distance[ci], ci))
            check[ci] = False

answer = []
for i in range(1, len(distance)):
    if distance[i] == k:
        answer.append(i)
    
if not answer:
    print(-1)
else:
    for i in answer:
        print(i)