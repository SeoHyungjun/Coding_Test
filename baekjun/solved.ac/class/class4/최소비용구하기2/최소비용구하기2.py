import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

board = [[] for _ in range(N+1)]

for _ in range(M):
    st, en, co = map(int, sys.stdin.readline().split())
    board[st].append((en, co))

start, end = map(int, sys.stdin.readline().split())

queue = []
heapq.heappush(queue, (0, start))
distance = [float('inf')] * (N+1)
distance[start] = 0
path = [[i] for i in range(N+1)]

while queue:
    cost, cur = heapq.heappop(queue)

    if cost > distance[cur]:
        continue

    for ne, co in board[cur]:
        if cost + co < distance[ne]:
            distance[ne] = cost + co
            heapq.heappush(queue, (distance[ne], ne))
            path[ne] = path[cur][:]
            path[ne].append(ne)

print(distance[end])
print(len(path[end]))
print(*path[end])
