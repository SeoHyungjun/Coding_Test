import sys
from collections import defaultdict, deque

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    rank = list(map(int, sys.stdin.readline().split()))

    graph = defaultdict(list)
    indegree = defaultdict(int)
    for i in range(N-1):
        graph[rank[i]] = rank[i+1:]
        indegree[rank[i+1]] = i+1

    M = int(sys.stdin.readline())
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())

        if a in graph[b]:
            graph[a].append(b)
            graph[b].remove(a)

            indegree[a] -= 1
            indegree[b] += 1
        else:
            graph[b].append(a)
            graph[a].remove(b)

            indegree[b] -= 1
            indegree[a] += 1

    queue = []
    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
            break

    answer = []
    while queue:
        cur = queue.pop()
        answer.append(cur)

        for i in graph[cur]:
            indegree[i] -= 1

            if indegree[i] == 0:
                queue.append(i)

    if len(answer) == N:
        print(*answer)
    else:
        print('IMPOSSIBLE')