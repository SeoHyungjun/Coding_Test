import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

board = {}
for i in range(N):
    board[i] = []

for _ in range(M):
    s, e, c = map(int, sys.stdin.readline().split())
    board[s-1].append((e-1, c))

answer = []
for i in range(N):
    queue = []
    heapq.heappush(queue, (0, i))

    distance = [float('inf')] * N
    distance[i] = 0

    while queue:
        cost, cur = heapq.heappop(queue)

        if cost > distance[cur]:
            continue

        for ne, co in board[cur]:
            if distance[cur] + co < distance[ne]:
                distance[ne] = distance[cur] + co
                heapq.heappush(queue, (distance[ne], ne))

    answer.append(distance)

for i in answer:
    print(*i)
