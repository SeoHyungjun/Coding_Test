import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()
for i in range(1, N+1):
    queue.append(i)

answer = []
while len(queue) > 1:
    answer.append(queue.popleft())
    queue.append(queue.popleft())
answer.append(queue.popleft())

print(*answer)