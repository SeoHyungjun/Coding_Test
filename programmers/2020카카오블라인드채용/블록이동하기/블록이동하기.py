# 2021-03-08 15:01 -> 

from collections import deque

def solution(board):
    answer = len(board)**2

    head = [0, 1]
    tail = [0, 0]
    direction = 'l' # 가로모양 l(left) , 세로모양 u(up)
    cnt = 0
    n = len(board)

    queue = deque()
    queue.append((head, tail, direction, cnt))

    while queue:
        cur_head, cur_tail, d, cnt= queue.popleft()
        #print(cur_head, cur_tail, cnt)

        if cur_head == (n-1, n-1) or cur_tail == (n-1, n-1):
            return cnt

        # 가로일 경우
        if d == 'l':
            # 오른쪽으로 한칸 갈 수 있으면
            if cur_head[1]+1 < n and board[cur_head[0]][cur_head[1]+1] == 0:
                next_head = (cur_head[0], cur_head[1]+1)
                next_tail = cur_head
                queue.append((next_head, next_tail, d, cnt+1))
            
            # 방향 전환이 가능하면?
            if cur_tail[0]+1 < n and board[cur_tail[0]+1][cur_tail[1]] == 0:
                next_head = (cur_tail[0]+1, cur_tail[1]+1)
                next_tail = cur_head
                d = 'u'
                queue.append((next_head, next_tail, d, cnt+1))
        
        # 세로일 경우
        else:
            # 아래로 내려갈 수 있으면
            if cur_head[0]+1 < n and board[cur_head[0]+1][cur_head[1]] == 0:
                next_head = (cur_head[0]+1, cur_head[1])
                next_tail = cur_head
                queue.append((next_head, next_tail, d, cnt+1))
            # 방향 전환이 가능하면?
            if cur_tail[1]+1 < n and board[cur_tail[0]][cur_tail[1]+1] == 0:
                next_head = (cur_tail[0]+1, cur_tail[1]+1)
                next_tail = cur_head
                d = 'l'
                queue.append((next_head, next_tail, d, cnt+1))

    # for b in board:
    #     print(b)

    return answer


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))