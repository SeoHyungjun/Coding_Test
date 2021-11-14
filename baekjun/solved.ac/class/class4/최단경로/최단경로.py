import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())

gra = [[] * V for _ in range(V)]
for _ in range(E):
    s, e, c = map(int, sys.stdin.readline().split())
    gra[s-1].append((e-1, c))

queue = []
heapq.heappush(queue, (0, start-1))
distance = [float('inf')] * V
distance[start-1] = 0
while queue:
    cost, index = heapq.heappop(queue)

    if cost > distance[index]:
        continue

    for ne, ne_co in gra[index]:
        ne_sum_cost = ne_co + cost
        if ne_sum_cost < distance[ne]:
            distance[ne] = ne_sum_cost
            heapq.heappush(queue, (distance[ne], ne))

for i in distance:
    if i == float('inf'):
        print('INF')
    else:
        print(i)

