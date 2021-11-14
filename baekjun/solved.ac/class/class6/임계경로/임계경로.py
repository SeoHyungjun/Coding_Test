import sys
from collections import deque

def solve():
    queue = deque()
    queue.append(start)

    while queue:
        cur = queue.popleft()

        for next, cost in graph[cur]:
            inDegree[next] -= 1
            distance[next] = max(distance[next], distance[cur] + cost)

            if not inDegree[next]:
                queue.append(next)

    visit = [True] * n
    answer = 0
    queue.append(end)
    while queue:
        cur = queue.popleft()

        for next, cost in backTrackinggraph[cur]:
            if distance[cur] - distance[next] == cost:
                answer += 1

                if visit[next]:
                    queue.append(next)
                    visit[next] = False

    return distance[end], answer

n = int(sys.stdin.readline())
graph = {i:[] for i in range(n)}
backTrackinggraph = {i:[] for i in range(n)}
inDegree = [0] * n
distance = [0] * n

m = int(sys.stdin.readline())
for _ in range(m):
    a, b, t = map(int, sys.stdin.readline().split())
    graph[a-1].append((b-1, t))
    backTrackinggraph[b-1].append((a-1, t))
    inDegree[b-1] += 1

start, end = map(int, sys.stdin.readline().split())
start, end = start - 1, end - 1

print(*solve(), sep = '\n')