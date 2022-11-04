import sys
sys.setrecursionlimit(100000)

def set_parent(cur, d):
    visit[cur] = True
    depth[cur] = d
    for child in graph[cur]:
        if visit[child]: continue
        parent[child][0] = cur
        set_parent(child, d+1)

def lca(a, b):
    if depth[a] > depth[b]: a, b = b, a

    for i in range(20, -1, -1):
        if depth[b] - depth[a] < (1 << i): continue
        b = parent[b][i]

    if a == b: return a

    for jump in range(20, -1, -1):
        if parent[a][jump] != parent[b][jump]:
            a = parent[a][jump]
            b = parent[b][jump]

    return parent[a][0]

N = int(sys.stdin.readline())
parent = [[0] * 21 for _ in range(N+1)]
visit = [False] * (N+1)
depth = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

set_parent(1, 0) # root = 1 부터 시작, root의 depth = 0
for i in range(1, 21):
    for j in range(1, N+1):
        parent[j][i] = parent[parent[j][i-1]][i-1]

M = int(sys.stdin.readline())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(lca(a, b))