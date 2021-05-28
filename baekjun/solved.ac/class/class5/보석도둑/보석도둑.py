import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
gam = []
bag = []

for i in range(N):
    M, V = map(int, sys.stdin.readline().split())
    heapq.heappush(gam, (M, V)) 

gam.sort(key = lambda x : (-x[1], x[0]))

for i in range(K):
    C = int(sys.stdin.readline())
    bag.append(C)

bag.sort()

avail = []
answer = 0
for i in bag:
    while gam and gam[0][0] <= i:
        heapq.heappush(avail, -heapq.heappop(gam)[1])

    if avail:
        answer -= heapq.heappop(avail)

print(answer)