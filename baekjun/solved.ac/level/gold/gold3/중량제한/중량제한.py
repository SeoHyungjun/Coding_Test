import sys
from collections import deque

def binary_search():
    answer = 1
    left, right = 1, 10000000000
    while left <= right:
        mid = (left + right) // 2
        if bfs(mid): 
            answer = mid
            left = mid + 1
        else: right = mid - 1

    return answer

def bfs(target):
    visited = [0 for _ in range(N+1)]
    visited[start] = 1
    queue = deque([start])
    while queue:
        u = queue.popleft()
        if u == end:
            return True
        for v, w in graph[u]:
            if not visited[v] and w >= target:
                visited[v] = 1
                queue.append(v)
    return False

N, M = map(int, sys.stdin.readline().split())
graph = [[] for i in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
start, end = map(int, sys.stdin.readline().split())

print(binary_search())