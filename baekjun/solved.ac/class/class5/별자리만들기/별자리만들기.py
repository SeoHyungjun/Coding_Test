import sys
import heapq

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def distance(arr, a, b):
    return ((arr[a][0] - arr[b][0])**2 + (arr[a][1] - arr[b][1])**2)**0.5

def solve():
    queue = []
    answer = 0
    for i in range(N):
        for j in range(i+1, N):
            heapq.heappush(queue, (distance(arr, i, j), i, j))

    while queue:
        cost, a, b = heapq.heappop(queue)

        if find_parent(a) == find_parent(b):
            continue
    
        answer += cost
        union(a, b)

    return answer

N = int(sys.stdin.readline())
parent = [i for i in range(N)]
arr = [list(map(float, sys.stdin.readline().split())) for _ in range(N)]
print('%.2f'%solve())