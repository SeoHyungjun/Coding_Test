import sys
import heapq

min_heap = []
max_heap = []
in_list = [False] * 100001
N = int(sys.stdin.readline())
for _ in range(N):
    P, L = map(int, sys.stdin.readline().split())
    heapq.heappush(min_heap, (L, P))
    heapq.heappush(max_heap, (-L, -P))
    in_list[P] = True

M = int(sys.stdin.readline())
for _ in range(M):
    com = sys.stdin.readline().split()

    if com[0] == 'recommend':
        if com[1] == '1':
            while not in_list[-max_heap[0][1]]:
                heapq.heappop(max_heap)
            print(-max_heap[0][1])

        elif com[1] == '-1':
            while not in_list[min_heap[0][1]]:
                heapq.heappop(min_heap)
            print(min_heap[0][1])
        
    elif com[0] == 'add':
        P, L = int(com[1]), int(com[2])
        while not in_list[-max_heap[0][1]]:
            heapq.heappop(max_heap)
        while not in_list[min_heap[0][1]]:
            heapq.heappop(min_heap)
        in_list[P] = True
        heapq.heappush(min_heap, (L, P))
        heapq.heappush(max_heap, (-L, -P))
        
    elif com[0] == 'solved':
        in_list[int(com[1])] = False