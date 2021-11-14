import sys
input = sys.stdin.readline
import heapq

# 도시수 n, 도로 수 m, 거리정보 k, 출발도시 x
n, m, k, x = map(int, input().split())

graph = [[float('inf') if i != j else 0 for i in range(n)] for j in range(n)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start-1][end-1] = 1

queue = []
heapq.heappush(queue, (x-1, 0))
distances = [float('inf')] * n
distances[x-1] = 0

while queue:
    city, distance = heapq.heappop(queue)

    for i in range(n):
        if graph[city][i] + distance < distances[i]:
            distances[i] = graph[city][i] + distance
            heapq.heappush(queue, (i, distances[i]))

if k not in distances:
    print(-1)
else:
    for i in range(n):
        if distances[i] == k:
            print(i+1)