import sys
import heapq

dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def dijkstra():
    queue = []
    heapq.heappush(queue, (board[0][0], 0, 0))

    distance = [[float('inf')] * N for _ in range(N)]
    distance[0][0] = board[0][0]

    while queue:
        cost, x, y = heapq.heappop(queue)

        if x == N - 1 and y == N - 1:
            return distance[x][y]

        for dx, dy in dir:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and distance[nx][ny] > board[nx][ny] + cost:
                distance[nx][ny] = board[nx][ny] + cost
                heapq.heappush(queue, (distance[nx][ny], nx, ny))

count = 1
while True:
    N = int(sys.stdin.readline())

    if N == 0:
        break

    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    print('Problem ' + str(count) + ':', dijkstra())
    count += 1