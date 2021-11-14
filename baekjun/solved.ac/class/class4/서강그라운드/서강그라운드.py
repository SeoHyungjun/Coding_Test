import sys
import heapq

N, M, R = map(int, sys.stdin.readline().split())
item = list(map(int, sys.stdin.readline().split()))

def dijsktra(start):
    distance = [float('inf')] * N
    distance[start] = 0
    heapq.heappush(queue, (0, start))

    while queue:
        co, cur = heapq.heappop(queue)

        if co > distance[cur]:
            continue

        for ne, cost in graph[cur]:
            if distance[ne] > co + cost:
                distance[ne] = co + cost
                heapq.heappush(queue, (distance[ne], ne))

    answer = 0
    for i in range(N):
        if distance[i] <= M:
            answer += item[i]

    return answer

graph = [[] for _ in range(N)]
for _ in range(R):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a-1].append((b-1, c))
    graph[b-1].append((a-1, c))

answer = 0
queue = []
for i in range(N):
    answer = max(answer, dijsktra(i))

print(answer)