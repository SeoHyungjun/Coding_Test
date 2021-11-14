import sys
import heapq
from typing import Mapping

T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())

    min_queue = []
    max_queue = []
    deleted = [False] * 1000001

    for id in range(k):
        com, num = sys.stdin.readline().split()

        if com == 'I':
            heapq.heappush(min_queue, (int(num), id))
            heapq.heappush(max_queue, (-1*int(num), id))
        
        elif com == 'D':
            if num == '-1':
                while min_queue:
                    _, id = heapq.heappop(min_queue)
                    if not deleted[id]:
                        deleted[id] = True
                        break

            elif num == '1':
                while max_queue:
                    _, id = heapq.heappop(max_queue)
                    if not deleted[id]:
                        deleted[id] = True
                        break

    while min_queue and deleted[min_queue[0][1]]:
        heapq.heappop(min_queue)
    while max_queue and deleted[max_queue[0][1]]:
        heapq.heappop(max_queue)

    if not min_queue and not max_queue:
        print('EMPTY')
    elif len(min_queue) == 1 and len(max_queue) == 1:
        num, _ = heapq.heappop(min_queue)
        print(num, num)
    else:
        min_num, _ = heapq.heappop(min_queue)
        max_num, _ = heapq.heappop(max_queue)
        print(-1*max_num, min_num)