# 210118 15:30 -> 16:45

from collections import deque

k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    
    graph = [[] for _ in range(v)]
    visit = [0 for _ in range(v)]
    answer = 0

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    for i in range(v):
        if visit[i] == 0:
            queue = deque()
            queue.append(i)
            visit[i] = 1

            while queue:
                cur = queue.popleft()

                for next in graph[cur]:
                    if visit[next] == 0:
                        visit[next] = visit[cur] * -1
                        queue.append(next)
                    elif visit[next] == visit[cur]:
                        answer = 1
                        break

    if answer == 0:
        print('YES')
    else:
        print('NO')