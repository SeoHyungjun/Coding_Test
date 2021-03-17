# 2021-03-12 16:42 -> 17:16

from collections import deque

def solution(board):
    answer = 0

    len_board = len(board)
    visit = []
    queue = deque()
    queue.append((0, 0, 0, 's'))
    visit = [[float('inf')] * len_board for _ in range(len_board)]
    print(visit)
    direction = [(0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u'), (1, 0, 'd')]

    while queue:
        cur_x, cur_y, cost, d = queue.popleft()
        print(cur_x, cur_y, cost, d)

        for dx, dy, dd in direction:
            if 0 <= cur_x + dx < len_board and 0 <= cur_y + dy < len_board and board[cur_x+dx][cur_y+dy] == 0:
                if d == 's' or d == dd:
                    if visit[cur_x + dx][cur_y + dy] >= cost+100:
                        queue.append((cur_x + dx, cur_y + dy, cost+100, dd))
                        visit[cur_x + dx][cur_y + dy] = cost+100
                else:
                    if visit[cur_x + dx][cur_y + dy] >= cost+600:
                        queue.append((cur_x + dx, cur_y + dy, cost+600, dd))
                        visit[cur_x + dx][cur_y + dy] = cost+600

    for i in visit:
        print(i)
    return visit[len_board-1][len_board-1]


board = [[0,0,0],[0,0,0],[0,0,0]]
board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
print(solution(board))