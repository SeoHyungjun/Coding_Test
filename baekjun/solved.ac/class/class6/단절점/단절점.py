import sys
sys.setrecursionlimit(10**9)

def dfs(here, is_root):
    global visit, index_visit, cut_vertex
    visit[here] = index_visit
    index_visit += 1
    min_index = visit[here]
    child = 0

    for next in graph[here]:
        if next in visit:
            min_index = min(min_index, visit[next])
            continue
        
        child += 1
        child_min_index = dfs(next, False)
        if not is_root and child_min_index >= visit[here]:
            cut_vertex.add(here)

        min_index = min(min_index, child_min_index)

    if is_root and child >= 2:
        cut_vertex.add(here)

    return min_index


V, E = map(int, sys.stdin.readline().split())
graph = {i+1:[] for i in range(V)}

for _ in range(E):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visit = {}
index_visit = 0
cut_vertex = set()

# 연결 그래프가 아닐수도 있으므로 모두 체크해야함
for i in range(1, V+1):
    if i not in visit:
        dfs(i, True)

print(len(cut_vertex))
if cut_vertex:
    print(*sorted(cut_vertex))