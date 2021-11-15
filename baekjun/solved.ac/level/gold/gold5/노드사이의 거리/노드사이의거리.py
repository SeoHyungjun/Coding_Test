import sys
from collections import defaultdict, deque

def find_distance(root, target):
    queue = deque()
    queue.append((root, 0))
    visit = set()
    visit.add(root)

    while queue:
        cur, cost = queue.popleft()

        if cur == target:
            return cost

        for next, next_cost in graph[cur]:
            if next in visit:
                continue

            visit.add(next)
            queue.append((next, cost + next_cost))

N, M = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for i in range(N-1):
    A, B, D = map(int, sys.stdin.readline().split())
    graph[A].append([B, D])
    graph[B].append([A, D])

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(find_distance(start, end))