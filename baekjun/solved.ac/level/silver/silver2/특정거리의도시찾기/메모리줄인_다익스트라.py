import sys
input = sys.stdin.readline
import heapq

# 도시수 n, 도로 수 m, 거리정보 k, 출발도시 x
n, m, k, x = map(int, input().split())

graph = {}
for i in range(n):
    graph[i] = []

for _ in range(m):
    start, end = map(int, input().split())
    graph[start-1].append(end-1)

queue = []
heapq.heappush(queue, (x-1, 0))
distances = [float('inf')] * n
distances[x-1] = 0

while queue:
    city, distance = heapq.heappop(queue)

    for ci in graph[city]:
        if distance + 1 < distances[ci]:
            distances[ci] = distance + 1
            heapq.heappush(queue, (ci, distances[ci]))

if k not in distances:
    print(-1)
else:
    for i in range(n):
        if distances[i] == k:
            print(i+1)