import sys
import heapq

N = int(sys.stdin.readline())

gr = [[] for _ in range(N)]

for _ in range(N-1):
    s, e, c = map(int, sys.stdin.readline().split())
    gr[s-1].append((e-1, c))
    gr[e-1].append((s-1, c))

def dij(i):
    queue = []
    heapq.heappush(queue, (0, i))
    distance = [float('inf')] * N
    distance[i] = 0

    while queue:
        cost, cur = heapq.heappop(queue)

        if cost > distance[cur]:
            continue

        for next, co in gr[cur]:
            if distance[next] > cost + co:
                distance[next] = cost + co
                heapq.heappush(queue, (distance[next], next))

    return (max(distance), distance.index(max(distance)))

print(dij(dij(0)[1])[0])