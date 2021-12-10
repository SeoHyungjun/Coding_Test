import sys
from collections import deque

input_string = sys.stdin.readline().rstrip()
size = input_string.count('b')
input_string += input_string
answer = size
queue = deque()

for i in range(len(input_string)):
    if queue and i - queue[0] >= size:
        queue.popleft()
    if input_string[i] == 'b':
        queue.append(i)
    answer = min(answer, size - len(queue))

print(answer)