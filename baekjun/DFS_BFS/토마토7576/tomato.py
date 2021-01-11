# 210111 14:25 -> 15:13 (약 50분...?)
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check_tomato(N, M, container):
    red_tomato = deque()

    for i in range(M):
        for j in range(N):
            if container[i][j] == 1:
                red_tomato.append((i, j))

    return red_tomato

def dfs(N, M, container):
    zero_cnt = 0
    for i in range(M):
        if 0 not in container[i]:
            zero_cnt += 1
    
    if zero_cnt == M:
        return 0

    red = check_tomato(N, M, container)

    while red:
        #print(day, red)
        #for i in range(M):
        #    print(container[i])

        for _ in range(len(red)):
            r = red.popleft()
            y = r[0]
            x = r[1]
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= nx < N and 0 <= ny < M and container[ny][nx] == 0:
                    container[ny][nx] = container[y][x] + 1
                    red.append((ny, nx))
        
    result = 0
    for i in range(M):
        if 0 in container[i]:
            return -1
        if max(container[i]) > result:
            result = max(container[i])

    return result-1

# 세로 M, 가로 N
N, M = map(int, input().split())

container = []
day = 0

for _ in range(M):
    container.append(list(map(int, input().split())))

print(dfs(N, M, container))