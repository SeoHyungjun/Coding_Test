import sys
sys.setrecursionlimit(10**9)

def change(a, b):
    if a < b:
        return (a, b)
    else:
        return (b, a)

def find_bridge(parent, here):
    global bridge, visit, index_visit
    visit[here] = index_visit
    index_visit += 1
    min_index = visit[here]

    for next in graph[here]:
        if parent != -1 and next == parent:
            continue

        if next in visit:
            min_index = min(min_index, visit[next])
            continue

        child_min_index = find_bridge(here, next)

        if child_min_index > visit[here]:
                bridge.add(change(here, next))

        min_index = min(min_index, child_min_index)

    return min_index


V, E = map(int, sys.stdin.readline().split())
graph = {i+1:[] for i in range(V)}
for _ in range(E):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

bridge = set()
visit = {}
index_visit = 0

find_bridge(-1, 1)
print(len(bridge))
for a in sorted(bridge, key=lambda x : (x[0], x[1])):
    print(*a)