import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()
indegree = [0]*(N+1)
arr = [[0]*(N+1) for _ in range(N+1)]
time = [0]*(N+1)

for i in range(1, N+1):
    _input = list(map(int, sys.stdin.readline().split()))
    time[i] = _input[0]
    for x in _input[1:-1]:
        arr[i][x] = 1
        indegree[i] += 1

for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    x = queue.popleft()
    t = 0
    for i in range(1, N+1):
        if arr[i][x] == 1:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
        if arr[x][i] == 1:
            t = max(time[i], t)
    time[x] += t

for i in time[1:]:
    print(i)