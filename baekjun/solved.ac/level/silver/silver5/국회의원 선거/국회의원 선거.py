import sys
import heapq

N = int(sys.stdin.readline())
dasom = -int(sys.stdin.readline())
queue = []
for _ in range(N-1):
    heapq.heappush(queue, -int(sys.stdin.readline()))

answer = 0
while queue and dasom >= queue[0]:
    cur = heapq.heappop(queue)
    if cur >= -1:
        continue
    
    heapq.heappush(queue, cur + 1)
    dasom -= 1
    answer += 1

print(answer)