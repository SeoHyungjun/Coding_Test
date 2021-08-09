import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(N)]
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
answer = 0

for i in range(M):
    if find(arr[i][0]) == find(arr[i][1]):
        answer = i+1
        break
    union(arr[i][0], arr[i][1])

print(answer)