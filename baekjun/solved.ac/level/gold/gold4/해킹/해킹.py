import sys
from collections import defaultdict
import heapq

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))

    distance = [float('inf')] * N
    distance[start] = 0

    while queue:
        sumCost, cur = heapq.heappop(queue)

        for next, cost in graph[cur]:
            nextCost = sumCost + cost
            if nextCost < distance[next]:
                distance[next] = nextCost
                heapq.heappush(queue, (nextCost, next))

    numHacked, maxTime = 0, 0
    for i in range(N):
        if distance[i] != float('inf'):
            numHacked += 1
            if distance[i] > maxTime:
                maxTime = distance[i]

    return numHacked, maxTime

T = int(sys.stdin.readline())
for _ in range(T):
    N, D, C = map(int, sys.stdin.readline().split())

    graph = defaultdict(list)
    for _ in range(D):
        a, b, s = map(int, sys.stdin.readline().split())
        graph[b-1].append((a-1, s))

    print(*dijkstra(C-1))