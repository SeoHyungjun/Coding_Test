import sys
import heapq
from collections import defaultdict

def dijkstra():
    queue = []
    heapq.heappush(queue, (0, 0))
    distance = [float('inf')] * N
    distance[0] = 0
    before = [-1] * N

    while queue:
        sumCost, cur = heapq.heappop(queue)

        for next in range(N):
            if cur != next and graph[cur][next] != float('inf') and distance[next] > sumCost + graph[cur][next]:
                distance[next] = sumCost + graph[cur][next]
                before[next] = cur
                heapq.heappush(queue, (distance[next], next))

    routine = []
    index = N-1
    while before[index] != -1:
        routine.append(index)
        index = before[index]
    routine.append(0)

    return distance[N-1], routine[::-1]

N, M = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().split())
    graph[a-1].append((b-1, t))
    graph[b-1].append((a-1, t))

normalTime, route = dijkstra()
answer = -1

for i in range(len(route)-1):

    banTime, _ = dijkstra()
    
    if banTime == float('inf'):
        answer = -1
        break
    answer = max(answer, banTime - normalTime)

print(answer)