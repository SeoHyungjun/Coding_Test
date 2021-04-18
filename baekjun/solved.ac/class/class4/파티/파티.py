import sys
import heapq

N, M, X = map(int, sys.stdin.readline().split())

graph = [[float('inf')]*N for _ in range(N)]
back_graph = [[float('inf')]*N for _ in range(N)]

for _ in range(M):
    st, en, co = map(int, sys.stdin.readline().split())
    graph[st-1][en-1] = co
    back_graph[en-1][st-1] = co

print(graph)
print(back_graph)

def dij(i, graph):
    queue = []
    heapq.heappush(queue, (0, i))

    distance = [float('inf')] * N
    distance[i] = 0
    visit = [False] * N
    visit[i] = True

    while queue:
        sum_cost, index = heapq.heappop(queue)
        visit[index] = True

        if distance[index] < sum_cost:
            continue

        for j in range(N):
            if not visit[j] and graph[index][j] + sum_cost < distance[j]:
                distance[j] = graph[index][j] + sum_cost
                heapq.heappush(queue, (distance[j], j))

    return distance

go = dij(X-1, graph)
back = dij(X-1, back_graph)

answer = 0
for i, j in zip(go, back):
    answer = max(answer, i+j)

print(answer)