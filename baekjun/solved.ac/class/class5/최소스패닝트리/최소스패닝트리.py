import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(s, e):
    s = find(s)
    e = find(e)
    if s < e:
        parent[e] = s
    else:
        parent[s] = e

V, E = map(int, sys.stdin.readline().split())
edge = []
parent = [i for i in range(V)]

for _ in range(E):
    S, E, C = map(int, sys.stdin.readline().split())
    edge.append((C, S-1, E-1))

edge.sort()

answer = 0
for c, s, e in edge:
    # 사이클이 발생하지 않는 경우 그래프에 포함
    if find(s) != find(e):
        answer += c
        union(s, e)

print(answer)