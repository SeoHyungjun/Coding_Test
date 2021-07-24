import sys
from collections import defaultdict, deque

N, M = map(int, sys.stdin.readline().split())
degree = [0] * (N+1)
dic = defaultdict(list)

for _ in range(M):
    arr = list(map(int, sys.stdin.readline().split()))

    for i in range(1, arr[0]):
        dic[arr[i]].append(arr[i+1])
        degree[arr[i+1]] += 1

queue = deque()
answer = []
for i in range(1, N+1):
    if degree[i] == 0:
        queue.append(i)

while queue:
    cur = queue.popleft()
    answer.append(cur)

    for next in dic[cur]:
        degree[next] -= 1
        if degree[next] == 0:
            queue.append(next)

if len(answer) < N:
    print(0)
else:
    print(*answer, sep='\n')