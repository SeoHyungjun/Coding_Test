# 210115 16:44 ->

from collections import deque

n, m = map(int, input().split())

arr = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    arr.append(list(map(int, input())))

queue = deque()
# 시작지점 0,0 과 벽을 뚫은 횟수 삽입 / 문제에서는 시작지점이 1,1로 나옴
queue.append((0, 0, 0))

def bfs():
    # visit을 통해서 이미 지나간 자리인지 확인
    # 이때 방문확인을 2차원으로해서 벽을 뚫은 상태일때와 뚫지 않은 상태에서 도착했을때를 각각 저장
    visit = [ [ [0]*2 for _ in range(m) ] for _ in range(n) ]
    # 0,0에서 (시작위치) 벽을 0번 뚫었으므로 [0][0][0] = 1
    visit[0][0][0] = 1

    while queue:
        # 현재 위치 x,y와 벽 뚫은 횟수 des
        x, y, des = queue.popleft()
        #if x == n-1 and y == m-1:
        #    return visit[x][y][des]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 지나갈 수 있는 공간이면
                if arr[nx][ny] == 0:
                    # 이미 방문했지만, 다른 경로를 통해서 왔을 때 더 적은 횟수로 도착한다면
                    if visit[nx][ny][des] != 0 and visit[nx][ny][des] > visit[x][y][des] + 1:
                        visit[nx][ny][des] = visit[x][y][des] + 1
                        queue.append((nx,ny,des))
                    # 방문 안했을 경우
                    if visit[nx][ny][des] == 0:
                        visit[nx][ny][des] = visit[x][y][des] + 1
                        queue.append((nx, ny, des))
                # 벽인데 벽 뚫을 기회가 있는 경우
                elif arr[nx][ny] == 1 and des == 0:
                    visit[nx][ny][des+1] = visit[x][y][des] + 1
                    queue.append((nx,ny,des+1))
        
    if visit[n-1][m-1][0] == 0 and visit[n-1][m-1][1] == 0:
        print('-1')
    elif visit[n-1][m-1][0] == 0 and visit[n-1][m-1][1] != 0:
        print(visit[n-1][m-1][1])
    elif visit[n-1][m-1][0] != 0 and visit[n-1][m-1][1] == 0:
        print(visit[n-1][m-1][0])
    else:
        print(min(visit[n-1][m-1]))

bfs()