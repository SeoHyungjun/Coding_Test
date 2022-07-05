import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()

for i in range(N, 0, -1):
    queue.appendleft(i)
    for j in range(i):
        queue.appendleft(queue.pop())

print(*queue)