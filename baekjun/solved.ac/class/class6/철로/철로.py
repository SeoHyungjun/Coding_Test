import sys
import heapq

N = int(sys.stdin.readline())
person = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    person.append((min(a,b), max(a,b)))
D = int(sys.stdin.readline())

person.sort(key=lambda x:(x[1], x[0]))
queue = []
answer = 0
for st, en in person:
    heapq.heappush(queue, (st, en))

    while queue:
        if queue[0][0] >= en - D:
            break
        heapq.heappop(queue)

    answer = max(answer, len(queue))

print(answer)
