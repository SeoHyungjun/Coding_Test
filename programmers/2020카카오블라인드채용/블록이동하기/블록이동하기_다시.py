# 2021-03-08 15:01 -> 

from collections import deque

def solution(board):
    n = len(board)
    # 좌우상하
    direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    rotate = [-1, 1]

    # 시작 위치
    start = sorted(((0,0), (0,1))) # 2x1칸 차지하므로 차지하는 칸 체크
    queue = deque()
    queue.append((sorted(start), 0))

    # 방문여부 체크하는 visit
    visit = []
    # 첫 위치 방문 표시
    visit.append(start)

    while queue:
        print(queue)
        (cur1, cur2), cnt = queue.popleft()
        cur = sorted((cur1, cur2))
        print(cur1, cur2, cnt)
        if cur1 == (n-1, n-1) or cur2 == (n-1, n-1):
            print('end')
            return cnt
        
        # 4방향 이동 체크
        for d in direction:
            next_x1, next_y1 = cur1[0] + d[0], cur1[1] + d[1]
            next_x2, next_y2 = cur2[0] + d[0], cur2[1] + d[1]
            next = sorted(((next_x1, next_y1), (next_x2, next_y2)))

            # 범위 안에있고
            if 0 <= next_x1 < n and 0 <= next_y1 < n and 0 <= next_x2 < n and 0 <= next_y2 < n:
                # 방문하지 않았고, 이동 가능하면
                if next not in visit and board[next_x1][next_y1] == 0 and board[next_x2][next_y2] == 0:
                    print('append 4', next)
                    queue.append((next, cnt+1))
                    visit.append(next)

        # 방향 전환 확인
        # 가로가 같으면 -> 가로배치
        if cur1[0] == cur2[0]:
            # 위 두칸, 아래 두칸 체크
            for d in rotate:
                next_x1, next_y1 = cur1[0] + d, cur1[1]
                next_x2, next_y2 = cur2[0] + d, cur2[1]
                if 0 <= next_x1 < n and 0 <= next_y1 < n and 0 <= next_x2 < n and 0 <= next_y2 < n:
                    next_L = sorted(((next_x1, next_y1), cur1))
                    next_R = sorted(((next_x2, next_y2), cur2))

                    # 위/아래 두칸이 비어있을 경우
                    if board[next_x1][next_y1] == 0 and board[next_x2][next_y2] == 0:
                        if next_L not in visit:
                            print('append g', next_L)
                            queue.append((next_L, cnt+1))
                            visit.append(next_L)
                        if next_R not in visit:
                            print('append g', next_R)
                            queue.append((next_R, cnt+1))
                            visit.append(next_R)

        # 세로가 같으면 -> 세로배치
        elif cur1[1] == cur2[1]:
            # 좌 뒤칸, 우 두칸 체크
            for d in rotate:
                next_x1, next_y1 = cur1[0], cur1[1] + d
                next_x2, next_y2 = cur2[0], cur2[1] + d
                if 0 <= next_x1 < n and 0 <= next_y1 < n and 0 <= next_x2 < n and 0 <= next_y2 < n:
                    next_L = sorted(((next_x1, next_y1), cur1))
                    next_R = sorted(((next_x2, next_y2), cur2))

                    # 좌/우 두칸이 비어있을 경우
                    if board[next_x1][next_y1] == 0 and board[next_x2][next_y2] == 0:
                        # 방문하지 않았을 경우 추가 
                        if next_L not in visit:
                            print('append s', next_L)
                            queue.append((next_L, cnt+1))
                            visit.append(next_L)
                        if next_R not in visit:
                            print('append s', next_R)
                            queue.append((next_R, cnt+1))
                            visit.append(next_R)


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))