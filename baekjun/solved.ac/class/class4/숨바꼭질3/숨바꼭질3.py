import sys
import heapq

arr = [float('inf')] * 100001

N, K = map(int, sys.stdin.readline().split())

arr[N] = 0
queue = []
heapq.heappush(queue, (0, N))

while queue:
    time, cur = heapq.heappop(queue)

    if 0 <= cur - 1 <= 100000 and arr[cur-1] > time+1:
        arr[cur-1] = time+1
        heapq.heappush(queue, (arr[cur-1], cur-1))

    if 0 <= cur + 1 <= 100000 and arr[cur+1] > time+1:
        arr[cur+1] = time+1
        heapq.heappush(queue, (arr[cur+1], cur+1)) 
    
    if 0 <= 2 * cur <= 100000 and arr[2*cur] > time:
        arr[2*cur] = time
        heapq.heappush(queue, (arr[2*cur], 2*cur))

print(arr[K])