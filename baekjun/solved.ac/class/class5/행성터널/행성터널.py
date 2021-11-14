import sys
import heapq

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

N = int(sys.stdin.readline())
parent = [i for i in range(N)]
x_list = []
y_list = []
z_list = []
for i in range(N):
    x, y, z = map(int, sys.stdin.readline().split())
    x_list.append((x, i))
    y_list.append((y, i))
    z_list.append((z, i))

x_list.sort()
y_list.sort()
z_list.sort()

queue = []
for i in range(1, N):
    heapq.heappush(queue, (abs(x_list[i-1][0] - x_list[i][0]), x_list[i-1][1], x_list[i][1]))
    heapq.heappush(queue, (abs(y_list[i-1][0] - y_list[i][0]), y_list[i-1][1], y_list[i][1]))
    heapq.heappush(queue, (abs(z_list[i-1][0] - z_list[i][0]), z_list[i-1][1], z_list[i][1]))

answer = 0
while queue:
    cost, a, b = heapq.heappop(queue)

    if find_parent(a) == find_parent(b):
        continue

    union(a, b)
    answer += cost

print(answer)