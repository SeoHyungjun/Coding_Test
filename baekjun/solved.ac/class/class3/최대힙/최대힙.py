import sys
import heapq

N = int(sys.stdin.readline())
queue = []

for _ in range(N):
    inp = sys.stdin.readline().rstrip()

    if inp == '0':
        if not queue:
            print(0)
        else:
            print(-1 * heapq.heappop(queue))

    else:
        heapq.heappush(queue, -1 * int(inp))
