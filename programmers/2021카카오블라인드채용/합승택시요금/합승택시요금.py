#2021-03-04 16:15 -> 17:04

import heapq

def solution(n, s, a, b, fares):
    answer = 0

    graph = [[float('inf')] * n for _ in range(n)]
    for fare in fares:
        st, en, val = fare
        graph[st-1][en-1] = val
        graph[en-1][st-1] = val

    answer = graph[s-1][a-1] + graph[s-1][b-1]
    dijkstra = []
    for i in range(n):
        re_cost = [float('inf')] * n
        re_cost[i] = 0
        queue = []
        heapq.heappush(queue, ((i, re_cost[i])))

        while queue:
            node, val = heapq.heappop(queue)
            for j in range(n):
                if val + graph[node][j] < re_cost[j]:
                    re_cost[j] = val + graph[node][j]
                    heapq.heappush(queue, (j, re_cost[j]))

        graph[i] = re_cost[:]

    for i in range(n):
        cost = 0
        if graph[i][a-1] + graph[i][b-1] + graph[s-1][i] < answer:
            answer = graph[i][a-1] + graph[i][b-1] + graph[s-1][i]

    return answer



print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
