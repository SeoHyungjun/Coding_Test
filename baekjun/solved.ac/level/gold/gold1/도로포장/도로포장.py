import sys
import heapq

def dijkstra():
    queue = []
    heapq.heappush(queue, (0, 0, 0))
    distance = [[float('inf')] * (K+1) for _ in range(N)]
    distance[0][0] = 0

    while queue:
        cost, pack, cur = heapq.heappop(queue)

        if distance[cur][pack] < cost:
            continue

        for next, to_cost in graph[cur]:
            # 포장을 안하고 가는 경우
            if distance[next][pack] > cost + to_cost:
                distance[next][pack] = cost + to_cost
                heapq.heappush(queue, (distance[next][pack], pack, next))
            # next로 가는 도로를 포장하는 경우
            if pack < K and distance[next][pack+1] > cost:
                distance[next][pack+1] = cost
                heapq.heappush(queue, (distance[next][pack+1], pack + 1, next))
                    
    return distance[N-1]

N, M, K = map(int, sys.stdin.readline().split())
graph = {i:[] for i in range(N)}

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a-1].append((b-1, c))
    graph[b-1].append((a-1, c))

print(min(dijkstra()))
