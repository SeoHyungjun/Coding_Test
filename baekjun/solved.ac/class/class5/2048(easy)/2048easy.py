import sys
import copy
from collections import deque

def move_left(board):
    for i in range(N):
        queue = deque()
        for j in range(N):
            if board[i][j] != 0:
                queue.append(board[i][j])
            board[i][j] = 0

        prev = 0
        where = 0
        while queue:
            cur = queue.popleft()
        
            if prev == 0:
                prev = cur
            else:
                if prev == cur:
                    board[i][where] = 2*prev
                    prev = 0
                else:
                    board[i][where] = prev
                    prev = cur
                where += 1
        if prev != 0:
            board[i][where] = prev
    return board

def move_right(board):
    for i in range(N):
        queue = deque()
        for j in range(N-1, -1, -1):
            if board[i][j] != 0:
                queue.append(board[i][j])
            board[i][j] = 0

        prev = 0
        where = N-1
        while queue:
            cur = queue.popleft()
        
            if prev == 0:
                prev = cur
            else:
                if prev == cur:
                    board[i][where] = 2*prev
                    prev = 0
                else:
                    board[i][where] = prev
                    prev = cur
                where -= 1
        if prev != 0:
            board[i][where] = prev
    return board

def move_up(board):
    for i in range(N):
        queue = deque()
        for j in range(N):
            if board[j][i] != 0:
                queue.append(board[j][i])
            board[j][i] = 0

        prev = 0
        where = 0
        while queue:
            cur = queue.popleft()
        
            if prev == 0:
                prev = cur
            else:
                if prev == cur:
                    board[where][i] = 2*prev
                    prev = 0
                else:
                    board[where][i] = prev
                    prev = cur
                where += 1
        if prev != 0:
            board[where][i] = prev
    return board

def move_down(board):
    for i in range(N):
        queue = deque()
        for j in range(N-1, -1, -1):
            if board[j][i] != 0:
                queue.append(board[j][i])
            board[j][i] = 0

        prev = 0
        where = N-1
        while queue:
            cur = queue.popleft()
        
            if prev == 0:
                prev = cur
            else:
                if prev == cur:
                    board[where][i] = 2*prev
                    prev = 0
                else:
                    board[where][i] = prev
                    prev = cur
                where -= 1
        if prev != 0:
            board[where][i] = prev
    return board

def max_in_board(board):
    answer = 0
    for i in board:
        answer = max(answer, max(i))
    return answer

def dfs(depth, board, path):
    if depth >= 5:
        return max_in_board(board)

    return max(dfs(depth + 1, move_left(copy.deepcopy(board)), path+'l'),
    dfs(depth + 1, move_right(copy.deepcopy(board)), path+'r'),
    dfs(depth + 1, move_up(copy.deepcopy(board)), path+'u'),
    dfs(depth + 1, move_down(copy.deepcopy(board)), path+'d'))
        
N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

print(dfs(0, board, ''))