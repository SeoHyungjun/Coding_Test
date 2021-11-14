import sys
import heapq

N = int(sys.stdin.readline())
queue = []
dic = {}

for _ in range(N):
    inp = sys.stdin.readline().rstrip()

    if inp == '0':
        if not queue:
            print(0)
        else:
            abs_num = heapq.heappop(queue)
            num = heapq.heappop(dic[abs_num])
            print(num)
            if len(dic[abs_num]):
                heapq.heappush(queue, abs_num)
            else:
                del dic[abs_num]

    else:
        abs_num = abs(int(inp))
        if abs_num not in dic:
            dic[abs_num] = []
            heapq.heappush(queue, abs_num)
        heapq.heappush(dic[abs_num], int(inp))