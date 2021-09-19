import sys
from collections import deque
sys.setrecursionlimit(10**6)

def find_lca(x, y):
    if d[x] < d[y]:
        x, y = y, x

    while d[x] != d[y]:
        x = p[x]

    while x != y:
        x = p[x]
        y = p[y]

    return x

MAX_NODE = 40001
tree = [[] for _ in range(MAX_NODE)]
d = [0] * MAX_NODE
p = [0] * MAX_NODE
dist = [0] * MAX_NODE

N = int(sys.stdin.readline())
for _ in range(N-1):
    a, b, c = map(int, sys.stdin.readline().split())
    tree[a].append([b, c])
    tree[b].append([a, c])

queue = deque()
queue.append(1)
p[1] = -1
d[1] = 0
dist[1] = 0

while queue:
    cur = queue.popleft()

    for next, cost in tree[cur]:
        if p[next] != 0:
            continue
        d[next] = d[cur] + 1
        p[next] = cur
        dist[next] = dist[cur] + cost
        queue.append(next)

M = int(sys.stdin.readline())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    lca = find_lca(a, b)
    print(dist[a] + dist[b] - 2*dist[lca])