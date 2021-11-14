import sys
import heapq
from collections import deque


def remove_min_path():
    queue = deque([en])
    visit = set()

    while queue:
        cur = queue.popleft()

        for before in before_best_node[cur]:
            if str(cur)+'to'+str(before) in visit:
                continue

            for i in range(len(graph[before])):
                if graph[before][i][0] == cur:
                    graph[before][i][1] = float('inf')
            queue.append(before)
            visit.add(str(cur)+'to'+str(before))


def dijkstra():
    global before_best_node
    queue = []
    heapq.heappush(queue, (0, st))

    distance = [float('inf')] * N
    distance[st] = 0

    while queue:
        cost, cur = heapq.heappop(queue)

        if distance[cur] < cost:
            continue

        for i in range(len(graph[cur])):
            next, next_cost = graph[cur][i]
            if next != cur and cost + next_cost < distance[next]:
                distance[next] = cost + next_cost
                queue.append((distance[next], next))

                before_best_node[next] = []
                before_best_node[next].append(cur)

            elif cost + next_cost == distance[next]:
                before_best_node[next].append(cur)

    return distance


while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break

    graph = {i : [] for i in range(N)}
    before_best_node = [[] for _ in range(N)]

    st, en = map(int, sys.stdin.readline().split())
    for _ in range(M):
        u, v, p = map(int, sys.stdin.readline().split())
        graph[u].append([v, p])

    dijkstra()
    remove_min_path()
    answer = dijkstra()
    print(-1 if answer[en] == float('inf') else answer[en])