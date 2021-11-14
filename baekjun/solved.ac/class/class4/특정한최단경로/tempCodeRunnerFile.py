import sys
import heapq

N, E = map(int, sys.stdin.readline().split())

graph = [[float('inf')]*N for _ in range(N)]
for _ in range(E):
    s, e, c = map(int, sys.stdin.readline().split())
    graph[s-1][e-1] = c
    graph[e-1][s-1] = c

mid1, mid2 = map(int, sys.stdin.readline().split())
mid1, mid2 = mid1-1, mid2-1

def dijsktra(index):
    queue = []
    heapq.heappush(queue, (0, index))
    distance = [float('inf')] * N
    distance[index] = 0

    while queue:
        cost, next = heapq.heappop(queue)

        if cost > distance[next]:
            continue

        for i in range(N):
            if cost + graph[index][i] < distance[i]:
                distance[i] = cost + graph[index][i]
                heapq.heappush(queue, (distance[i], i))

    return distance

st = dijsktra(0)
v1 = dijsktra(mid1)
v2 = dijsktra(mid2)

answer = min(st[mid1] + v1[v2] + v2[N-1], st[mid2] + v2[v1] + v1[N-1])

print(answer if answer < float('inf') else -1)