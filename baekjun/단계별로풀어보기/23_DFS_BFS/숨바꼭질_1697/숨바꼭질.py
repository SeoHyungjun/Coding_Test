# 210115 15:50 -> 해설 참조...
# xxxxxxxxxxxxxxxxxxxxxxxxx아마도 dfs?  
# bfs....

from collections import deque

n, k = map(int, input().split())

# 100000칸 이동가능하므로 
MIN = 100001
visit = [0 for _ in range(MIN)]

queue = deque()
queue.append((n, 0))

answer = MIN

while queue:
    cur, time = queue.popleft()
    visit[cur] = 1

    if cur == k:
        answer = time
        break

    #print(cur)

    if cur + 1 < MIN and visit[cur + 1] == 0:
        queue.append((cur+1, time+1))
    if visit[cur - 1] == 0 and cur - 1 >= 0:
        queue.append((cur-1, time+1))
    if cur * 2 < MIN and visit[cur * 2] == 0:
        queue.append((cur*2, time+1))

    answer += 1

print(answer)

