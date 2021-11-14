import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]
degree = [0] * N

queue = []
answer = []

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A-1].append(B-1)
    degree[B-1] += 1

for i in range(N):
    if degree[i] == 0:
        heapq.heappush(queue, i)

while queue:
    num = heapq.heappop(queue)
    answer.append(num+1)

    for i in graph[num]:
        degree[i] -= 1
        if degree[i] == 0:
            heapq.heappush(queue, i)

print(*answer)