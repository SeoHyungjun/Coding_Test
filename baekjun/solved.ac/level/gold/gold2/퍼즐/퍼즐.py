# 20:17 ~
import sys
from collections import deque

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs(arr):
    queue = deque()
    queue.append((0, arr))
    visit = {arr}

    while queue:
        cnt, cur = queue.popleft()

        if cur == target:
            return cnt

        zero = cur.find('0')
        x, y = zero//3, zero%3
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < 3 and 0 <= ny < 3):
                continue

            new_zero = nx*3 + ny
            new_cur = list(cur)
            new_cur[zero], new_cur[new_zero] = new_cur[new_zero], new_cur[zero]
            new_cur = ''.join(new_cur)
            if new_cur not in visit:
                visit.add(new_cur)
                queue.append((cnt + 1, new_cur))
        
    return -1

answer = 0
target = '123456780'
cur = (sys.stdin.readline() + sys.stdin.readline() + sys.stdin.readline()).replace(' ', '').replace('\n', '')

print(bfs(cur))