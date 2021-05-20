import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())


time = [float('inf')] * 100001
time[N] = 0
way = [0] * 100001
way[N] = 1

queue = deque()
queue.append((N, 0))

while queue:
    cur, cost = queue.popleft()

    if cur == K:
        continue

    next_list = [cur-1, cur+1, cur*2]

    for ne in next_list:
        if 0 <= ne <= 100000:
            if cost + 1 == time[ne]:
                way[ne] += 1
                queue.append((ne, cost+1))

            elif cost + 1 < time[ne]:
                time[ne] = cost + 1
                way[ne] = 1
                queue.append((ne, cost+1))

print(time[K])
print(way[K])