import sys
from collections import deque
import heapq

N, M = map(int, sys.stdin.readline().split())
move = {}

for _ in range(N+M):
    x, y = map(int, sys.stdin.readline().split())
    move[x] = y

def bfs(start, cnt):
    visit = [False] * 101
    queue = []
    heapq.heappush(queue, (cnt, start))
    visit[start] = True

    while queue:
        cnt, cur = heapq.heappop(queue)

        if cur == 100:
            return cnt

        if cur in move:
            heapq.heappush(queue,(cnt, move[cur]))
            visit[move[cur]] = True

        else:
            for i in range(1, 7):
                if 1 <= cur + i <= 100 and (not visit[cur + i]):
                    heapq.heappush(queue, (cnt+1, cur+i))
                    visit[cur+i] = True

print(bfs(1, 0))