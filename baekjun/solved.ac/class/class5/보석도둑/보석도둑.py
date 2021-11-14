import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
gam = []
bag = []

for i in range(N):
    M, V = map(int, sys.stdin.readline().split())
    heapq.heappush(gam, (M, V)) 

for i in range(K):
    bag.append(int(sys.stdin.readline()))
bag.sort()

avail = []
answer = 0
for i in bag:
    while gam and gam[0][0] <= i:
        heapq.heappush(avail, -heapq.heappop(gam)[1])

    if avail:
        answer -= heapq.heappop(avail)

    elif not gam:
        break

print(answer)