import sys
import heapq

N = int(sys.stdin.readline())
lesson = []
for _ in range(N):
    _, b, c = map(int, sys.stdin.readline().split())
    lesson.append((b, c))

lesson.sort(key=lambda x: (x[0], x[1]))

queue = []
for s, e in lesson:
    if queue and queue[0] <= s:
        heapq.heappop(queue)

    heapq.heappush(queue, e)

print(len(queue))