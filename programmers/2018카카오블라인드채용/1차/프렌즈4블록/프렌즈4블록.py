# 2021-02-23 13:56 -> 14:51

from collections import deque

def check_board(m, n, board):
    queue = deque()

    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] != '0' and board[i][j] == board[i+1][j] and board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j+1]:
                queue.append((i, j))
    return queue

def delete_queue(answer, queue, board):
    dx = [0, 1, 0, 1]
    dy = [0, 0, 1, 1]

    while queue:
        count = 0
        x, y = queue.popleft()
        
        for i in range(4):
            if board[x+dx[i]][y+dy[i]] != '0':
                count += 1
            #board[x+dx[i]][y+dy[i]] = '0' 
            board[x+dx[i]][y+dy[i]] = '0'

        answer += count
    return answer

def down_board(m, n, board):
    for j in range(n):
        for i in range(1, m):
            if board[i][j] == '0':
                for k in range(i, 0, -1):
                    board[k][j] = board[k-1][j]
                board[0][j] = '0'


    return 0

def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])

    while True:
        queue = check_board(m, n, board)
        if not queue:
            break
        
        answer = delete_queue(answer, queue, board)
        down_board(m, n, board)

    return answer



m = 4
n = 5
board = ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']
m = 6
n = 6
board = ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']
print(solution(m, n, board))