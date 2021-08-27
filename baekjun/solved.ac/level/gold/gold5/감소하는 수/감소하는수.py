import sys
from collections import deque

def solve():
    if N < 10:
        return N
    else:
        queue = deque()
        for i in range(1, 10):
            queue.append(i)
        cnt = 9

        while queue:
            cur = queue.popleft()

            for i in range(0, cur%10):
                if cnt + 1 == N:
                    return cur*10 + i
                queue.append(cur*10 + i)
                cnt += 1
        
    return -1

N = int(sys.stdin.readline())
print(solve())