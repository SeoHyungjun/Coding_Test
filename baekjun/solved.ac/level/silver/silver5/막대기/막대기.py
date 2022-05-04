import sys
import heapq

X = int(sys.stdin.readline())

sticks = [64]
heapq.heapify(sticks)

while sum(sticks) != X:
    if sum(sticks) > X:
        min_stick = heapq.heappop(sticks)
        
        if sum(sticks) + min_stick/2 < X:
            heapq.heappush(sticks, min_stick/2)
        heapq.heappush(sticks, min_stick/2)

print(len(sticks))