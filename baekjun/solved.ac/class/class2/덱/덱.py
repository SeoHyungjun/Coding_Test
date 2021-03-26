from collections import deque
import sys

n = int(sys.stdin.readline())

queue = deque()

for _ in range(n):
    inp = sys.stdin.readline().split()

    if inp[0] == 'push_front':
        queue.appendleft(inp[1])

    elif inp[0] == 'push_back':
        queue.append(inp[1])

    elif inp[0] == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print('-1')

    elif inp[0] == 'pop_back':
        if queue:
            print(queue.pop())
        else:
            print('-1')

    elif inp[0] == 'size':
        print(len(queue))

    elif inp[0] == 'empty':
        if queue:
            print('0')
        else:
            print('1')

    elif inp[0] == 'front':
        if not queue:
            print('-1')
        else:
            a = queue.popleft()
            print(a)
            queue.appendleft(a)

    elif inp[0] == 'back':
        if not queue:
            print('-1')
        else:
            a = queue.pop()
            print(a)
            queue.append(a)