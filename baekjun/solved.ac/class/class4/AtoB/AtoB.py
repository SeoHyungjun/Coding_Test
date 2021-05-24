import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())

queue = deque()
queue.append((1, A))
answer = -1

while queue:
    cost, cur = queue.popleft()

    if cur == B:
        answer = cost
        break

    if cur * 2 < int(10e9) and cur * 2 <= B:
        queue.append((cost+1, cur*2))

    if cur * 10 + 1 < int(10e9) and cur * 10 + 1 <= B:
        queue.append((cost+1, cur*10 + 1))

print(answer)