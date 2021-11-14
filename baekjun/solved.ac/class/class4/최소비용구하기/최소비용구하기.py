import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

gr = [[] for _ in range(N)]
for _ in range(M):
    st, en, co = map(int, sys.stdin.readline().split())
    gr[st-1].append((en-1, co))

st, en = map(int, sys.stdin.readline().split())
st, en = st-1, en-1

queue = []
heapq.heappush(queue, (0, st))
distance = [float('inf')] * N
distance[st] = 0

while queue:
    cost, city = heapq.heappop(queue)

    if cost > distance[city]:
        continue

    for ne, co in gr[city]:
        new_cost = cost + co
        if new_cost < distance[ne]:
            distance[ne] = new_cost
            heapq.heappush(queue, (distance[ne], ne))

print(distance[en])