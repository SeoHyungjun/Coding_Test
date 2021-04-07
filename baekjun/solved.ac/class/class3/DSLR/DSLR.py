import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    
    queue = deque([(A, '')])
    visit = [False] * 10000
    visit[A] = True

    while queue:
        cur, history = queue.popleft()

        if cur == B:
            print(history)
            break

        else:
            if not visit[(cur*2) % 10000]:
                queue.append(( (cur*2) % 10000, history + 'D' ))
                visit[(cur*2) % 10000] = True
            if not visit[(cur - 1 + 10000) % 10000]:
                queue.append(( (cur - 1 + 10000) % 10000, history + 'S'))
                visit[(cur*2) % 10000] = True
            if not visit[(cur%1000*10 + cur//1000)]:
                queue.append(( (cur%1000*10 + cur//1000), history + 'L'))
                visit[(cur%1000*10 + cur//1000)] = True
            if not visit[(cur%10*1000 + cur//10)]:
                queue.append(( (cur%10*1000 + cur//10), history + 'R'))
                visit[(cur%10*1000 + cur//10)] = True

