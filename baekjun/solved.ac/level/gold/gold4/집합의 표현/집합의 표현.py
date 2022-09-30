import sys
sys.setrecursionlimit(10**9)

def union(a, b):
    a, b = find(a), find(b)
    if a < b: parent[b] = a
    else: parent[a] = b

def find(a):
    if a == parent[a]: return a
    parent[a] = find(parent[a])
    return parent[a]

N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(0, N+1)]
for _ in range(M):
    com, a, b = map(int, sys.stdin.readline().split())
    if com == 0:
        union(a, b)
        continue
    print("YES" if find(a) == find(b) else "NO")